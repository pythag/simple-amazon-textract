# simple-amazon-textract
A docker container that OCRs 1 or more images into a regular text file using Amazon's Textract service

## TLDR;
Usage:
1. Install docker & docker-compose (on Debian apt install docker-compose)
2. Make sure your AWS credentials and config are correctly setup in ~/.aws/
3. Place the images you want to convert in the images directory (supported types: .jpg, .jpeg, .png)
4. Run docker-compose up
5. Grab the result from images/result.txt

## Intro
This container was bourne of of frustration from trying to find a simple yet accurate command line driven OCR.

I stumbled upon Amazon's Textract service and using their online demo was able to determine that it was much more accurate than other OCR software I'd tried (e.g. Tesseract). The online demo in fact did everything I required of it (turned an image into a raw text file), however there was no way to run this from a batch process.

Amazon provide Python libraries so it should be trivial to automate calls to AWS Textract, however Python package management bit me hard and hours were wasted trying to get this to run natively.

In the end I created this trivial docker container (with simple Python script to call the AWS Textract library). I've kept everything as minimal as possible to provide the path of least resistance to usage.

## Getting started
If you're reading this because you want to OCR something and the regular tools aren't cutting it BE AWARE that you will need an AWS account. There is a bit of a learning curve required to even create and use an AWS account, so this isn't going to be a 5 minute solution.

If you already have an AWS account then this task should be pretty trivial.

### Setting up an AWS account
Follow steps 1 and 2 in this guide published by Amazon:
https://docs.aws.amazon.com/textract/latest/dg/getting-started.html

Having followed these you should end up with a '.aws' directory in your home directory. It should contain a credentials file (/home/myuser/.aws/credentials) that looks roughly as follows:
```
[default]
aws_access_key_id = ....................
aws_secret_access_key = ......................../...............
```
You should also have a config file (/home/myuser/.aws/config) that specifies the region:
```
[default]
region = eu-west-1
```

### Preparing the files for OCR
Inside this project is in 'images' subdirectory - place the images you want to convert to text in here. The script does sort the list of files found here alphabetically before running the OCR, so if you have multiple pages then name them so they sort cleanly, e.g. 'page-001.jpg', 'page-002.jpg'....
The script will look for files that end in '.jpg', '.jpeg' and '.png'.

### Running the conversion
Whilst in the directory you downloaded this project to simply run:
```
docker-compose up
```
After the container is built it takes around 5 seconds per image to convert... during the conversion process you don't see any output, so don't be alarmed if nothing appears to be happening.

### Getting the output
When the container runs it populates the file **images/result.txt** with the decoded text.

### Cost
Up to date pricing can be found here:
https://aws.amazon.com/textract/pricing/

At the timing of writing this the cost is **$1.50 per 1000 pages**.
