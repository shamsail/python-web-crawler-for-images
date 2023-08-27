# Web Crawler Script

This Python script is a simple web crawler that extracts images from web pages and recursively explores links to a specified depth level.

## Features

- Crawls web pages to extract images and follow links up to a specified depth level.
- Stores results in a JSON file in the following format:

```
{ 
    "results" : [
        { 
            "imageUrl": "string",
            "sourceUrl": "string // the page url this image was found on",
            "depth": "number // the depth of the source at which this image was found on"
        }
    ]
}
```

## Requirements

- Python 3.x
- Required Python packages can be installed using the provided `requirements.txt` file.

## Setup

1. **Clone this repository:**

```
git clone https://github.com/shamsail/python-web-crawler-for-images.git
cd web-crawler
```

2. **Create and activate a virtual environment (recommended):**

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the required packages using pip:**

```
pip install -r requirements.txt
```


## Usage

1. **Run the script using the following command:**

```
python crawler.py <start_url> <depth>
```

Replace `<start_url>` with the URL from which you want to start crawling, and `<depth>` with the desired depth level.

2. **The script will crawl the specified URL and explore links up to the specified depth, while extracting images. The results will be stored in a file named `results.json` in the same directory.**

## Example

To crawl a website starting from the URL `https://www.example.com/` and explore links up to a depth of 2, run the following command:

```
python crawler.py https://www.example.com/ 2
```

