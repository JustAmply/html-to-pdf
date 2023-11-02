> [!WARNING]  
> Not actively maintained. I found and use the API of [StirlingPDF](https://github.com/Frooodle/Stirling-PDF) with a similar feature as of now.


# html-to-pdf
Converts HTML to a PDF file

## Build
`docker build -t html-to-pdf .`

## Run
`docker run -p 5000:5000 -d html-to-pdf `

## Usage

### WebUI
Website accessible on port 5000
`http://localhost:5000/`

### API
Attach HTML as body to the POST-Request to
`http://localhost:5000/api/html-to-pdf`

Returns the PDF file as response
