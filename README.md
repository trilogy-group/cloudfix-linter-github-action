# Github Action for CloudFix Linter-Terraform

## Working
1. This action assumes the user will have the terraform.tfstate file in the repo and doesn't needs terraform initialization.  
2. Action creates Mock cloudfix recommendations.  
3. The generated mock cloudfix recommendations are then put as comments in the repo.

## Steps of the Job in workflow:
```
on:
  pull_request:

runs:
  using: composite
  steps:
    - name: Checkout
      uses: actions/checkout@v3
      with:
        repository: trilogy-group/cloudfix-linter-github-action
        path: mainRepo

    - name: Comment Reccomendation
      id: prcomment
      env:
        GH_TOKEN: ${{ inputs.GITHUB_TOKEN }}
        CLOUDFIX_USERNAME: ${{ inputs.cloudfix_username }}
        CLOUDFIX_PASSWORD: ${{ inputs.cloudfix_password }}
        ENABLE_MOCK_RECOMMENDATION: "${{ inputs.mock_recommendations }}"
        TERRAFORM_BINARY_PATH: ${{ inputs.terraform_binary_path }}
        pr_number: ${{ inputs.pr_number }}
        repository: ${{ inputs.repository }}
      run: echo $ENABLE_MOCK_RECOMMENDATION; sh mainRepo/script.sh
      shell: bash
``` 
   
1. Checking out current repo using [checkout](https://github.com/marketplace/actions/checkout) action in $GITHUB_WORKSPACE under mainRepo name.
2. Creating recommendatiions by running the script.sh script
  + Generating mock recommandations via script (The tf.show file should be present to create recommendations)
  + Installing tflint and cloudfix-linter 
  + Initializing cloudfix-linter 
  + Putting recommendations over the resources
  + Making comments from the recommendations
