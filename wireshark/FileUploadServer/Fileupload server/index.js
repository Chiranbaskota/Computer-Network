import fs from "fs";
import http from "http";
import path from "path"
import { fileURLToPath } from "url";


function handleFileUpload(req, res) {
    // Get the boundary from the content-type header
    const boundary = getBoundary(req.headers['content-type']);
   
    let rawData = '';
    req.on('data', (chunk) => {
        rawData += chunk;
    });

    // When all data is received
    req.on('end', () => {
        // Split the raw data into parts using the boundary
        const parts = rawData.split(boundary).filter(part => part.trim() !== '--' && part.trim() !== '');
        // Find the part that contains the file
        const filePart = parts.find(part => part.includes('filename'));

        // If the file part is found
        if (filePart) {
            // Extract the file data
            const start = filePart.indexOf('\r\n\r\n') + 4;
            const end = filePart.lastIndexOf('\r\n');
            const fileData = filePart.substring(start, end);

            // Extract the filename
            const filename = extractFilename(filePart);

            // Get the current directory
            const __filename = fileURLToPath(import.meta.url);
            const __dirname = path.dirname(__filename);
            // Create the file path
            const filepath = path.join(__dirname, 'uploads', filename);


            // Write the file to the uploads directory
            fs.writeFile(filepath, fileData, 'binary', (err) => {
                if (err) {
                    res.statusCode = 500;
                    res.end('Internal Server Error');
                    return;
                }
                console.log('File uploaded successfully')
                res.statusCode = 200;
                res.end('File uploaded successfully');
            });
        } else {
            res.statusCode = 400;
            res.end('Bad Request');
        }
    });
}
// Get the boundary from the content-type header
function getBoundary(contentType) {
    const items = contentType.split(';');
    for (let i = 0; i < items.length; i++) {
        const item = items[i].trim();
        if (item.startsWith('boundary=')) {
            return '--' + item.split('=')[1];
        }
    }
    return '';
}
// Extract the filename from the part
function extractFilename(part) {
    const filenameMatch = part.match(/filename="(.+?)"/);
    if (filenameMatch) {
        return filenameMatch[1];
    }
    return 'unknown';
}

async function showUploadForm(res) {
    res.setHeader('Content-Type', 'text/html');
    res.write(`
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload File</button>
        </form>
    `);
    res.end();
}


const server = http.createServer((req, res) => {
    if (req.url == '/upload' && req.method == 'POST') {
        handleFileUpload(req, res);
    }
    else if (req.url == '/' && req.method == 'GET') {
        showUploadForm(res);
    }
    else {
        res.statusCode = 404;
        res.end('Page Not Found');
    }
});

server.listen(3000, () => {
    console.log('Server is running on port 3000');
    console.log('http://localhost:3000');
});

