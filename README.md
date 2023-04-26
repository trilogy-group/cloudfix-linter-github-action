# Github Action for CloudFix Linter-Terraform

## Working
1. This action assumes that it is running after terraform init has been performed, and will expect the terraform state to be accessible through `terraform show` command.
2. Action runs the cloudfix-linter CLI and fetches recommendations.  
3. The generated Cloudfix recommendations are then put as a comment on the PR.

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
2. Creating recommendations by running the script.sh script
   + Installing cloudfix-linter CLI
   + Initializing cloudfix-linter for the current working directory 
   + Getting recommendations using the cloudfix-linter CLI
   + Dropping a comment on the PR showing the recommendations

*Note: Provides mock recommandations (if `mock_recommendations` input is st to true)*