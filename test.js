const { exec } = require('child_process');

// Replace with the actual YouTube video URL
const videoUrl = 'https://www.youtube.com/watch?v=example';

exec(`python test.py "${videoUrl}"`, (error, stdout, stderr) => {
    if (error) {
        console.error(`Execution Error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`Python Error: ${stderr}`);
        return;
    }
    console.log(`Output:\n${stdout}`);
});
