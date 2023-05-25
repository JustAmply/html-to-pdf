# html-to-pdf
 Converts HTML to a PDF file

## Build
`docker build -t html-to-pdf .`

## Run
`docker run -it html-to-pdf`

## Usage

### WebUI
Website accessible on port 5000
`http://localhost:5000/`

### API
Attach HTML as body to the POST-Request to
`http://localhost:5000/api/html-to-pdf`

Returns the PDF file as response