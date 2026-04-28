# User Manual

## Introduction
This application exposes the files located in the `files` folder via an nginx server.

## Main Features
- Access JSON and PDF files through browser or HTTP tools
- No user interface: access is direct via URL

## Usage Examples
- To view a file: `http://<ingress_hostname>/static/contract/ContractTemplate1.json`
- To download a PDF: `http://<ingress_hostname>/static/pdf/BillingSchema1.pdf`

## Tips
- Organize files in the `files` folder for easier navigation
- Update files without restarting the server (changes are immediate)

## FAQ
**Q: I don't see updated files.**
A: Make sure to refresh the page or clear your browser cache.

**Q: I get a 404 error.**
A: Check that the file exists in the `files` folder and the name is correct.
