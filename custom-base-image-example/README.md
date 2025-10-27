# Custom Base Image Example

This directory reproduces the steps from the “Standard Truss” tab in
`docs/index.mdx`.

## Usage

1. **Build the image**
   ```bash
   truss image build . --tag custom-base-image-example:latest
   ```
2. **Run it locally**
   ```bash
   truss image run . --tag custom-base-image-example:latest --port 8080
   ```
3. **Send the sample request**
   ```bash
   curl -X POST http://localhost:8080/v1/models/custom-base-image-example:predict \
     -H 'Content-Type: application/json' \
     -d '{"inputs": [1, 2, 3]}'
   ```
   Expected response: `[2, 4, 6]`.
