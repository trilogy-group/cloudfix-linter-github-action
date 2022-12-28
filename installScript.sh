#! /bin/bash


Arch=$(uname -m)

if [[ "$Arch" == "x86_64" || "$Arch" == "amd64" ]]; then
    PLATFORM=linux_amd64
elif [[ "$Arch" == "aarch64" || "$Arch" == "arm64" ]]; then
    PLATFORM=linux_arm64
elif [[ "$Arch" == "i686" || "$Arch" == "i386" ]]; then
    PLATFORM=linux_386
elif [ "$Arch" = "armhf" ]; then
    PLATFORM=linux_arm
else 
    echo "Unsupported platform"
    exit 1
fi

mkdir cloudfix-linter
cd cloudfix-linter

#Installing tflint 
# higher version have breaking changes to the plugin system and hence we can't install them without changing the plugin
echo "Installing tflint"
export TFLINT_VERSION=v0.39.3
(wget https://github.com/terraform-linters/tflint/releases/download/${TFLINT_VERSION}/tflint_${PLATFORM}.zip \
  && unzip tflint_${PLATFORM}.zip \
  && rm tflint_${PLATFORM}.zip)

# Install cloudfix-linter
echo "Installing cloudfix-linter"
(wget https://github.com/trilogy-group/cloudfix-linter-developer/releases/latest/download/cloudfix-linter-developer_${PLATFORM} \
  && mv cloudfix-linter-developer_${PLATFORM} cloudfix-linter)

chmod 777 cloudfix-linter
chmod 777 tflint

export CLOUDFIX_FILE=true 
export CLOUDFIX_TERRAFORM_LOCAL=true
cd ..