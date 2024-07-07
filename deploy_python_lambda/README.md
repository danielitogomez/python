## Setup Instructions

### Setting up AWS Credentials

1. **Create an IAM user** with programmatic access and attach the `AWSLambdaFullAccess` policy.
2. **Store the AWS credentials**:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Region
   Store these credentials in your GitHub repository's secrets under `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION` (The region can be just a env var, or simple hardcoded).

### Creating the Lambda Function in AWS

Follow these steps to set up your Lambda function in the AWS Management Console:

1. **Log into the AWS Management Console** and navigate to the Lambda service.
2. **Create a new Lambda function**:
   - Click on **Create function**.
   - Select **Author from scratch**.
   - Enter a function name, e.g., `lambda_function`.
   - For the runtime, select **Python 3.8** or the version you used in your development.
   - Choose or create a new role from template(s) that grants the necessary permissions to run your Lambda function. This role should include at least basic execution permissions.
   - Click on **Create function**.

3. **Configure function code**:
   - After creating the function, you can initially upload your `lambda_function.py` manually to test. Later, this process will be managed by GitHub Actions. (This is not really necesary)
   - Use the inline editor in the AWS Console for a quick setup or upload a ZIP file if your function has dependencies. (This is not really necesary)

4. **Set the handler**:
   - Ensure that the handler matches the filename and method in your code, e.g., `lambda_function.lambda_handler`.

### Configuring GitHub Actions

- The GitHub Actions workflow is set up to run automatically on any push to the main branch, triggering the deployment of the Lambda function.

### Running the Function Locally

To test the function locally, run:

```bash
python lambda_function.py
```