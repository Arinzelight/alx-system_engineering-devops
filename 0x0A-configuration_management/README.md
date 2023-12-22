# 0x0A. Configuration Management

This repository provides instructions for configuring Puppet, a widely used configuration management tool. It also includes steps for installing Puppet-lint, a tool for checking your Puppet code against recommended style guidelines.

## Puppet Installation

To install Puppet, follow the steps below:

1. Update the package repository:

    ```bash
    $ sudo apt-get update
    ```

2. Install Ruby and other required dependencies:

    ```bash
    $ sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades
    $ sudo apt-get install -y ruby-augeas
    $ sudo apt-get install -y ruby-shadow
    ```

3. Install Puppet:

    ```bash
    $ sudo apt-get install -y puppet
    ```

## Puppet-lint Installation

Puppet-lint is a tool for checking your Puppet code against the recommended style guidelines. To install Puppet-lint, follow the steps below:

1. Install the `gem` package manager:

    ```bash
    $ sudo apt-get install -y rubygems
    ```

2. Install Puppet-lint using `gem`:

    ```bash
    $ gem install puppet-lint
    ```

## Usage

### Puppet

After installing Puppet, you can use it to manage your infrastructure's configuration. Refer to the [official Puppet documentation](https://puppet.com/docs/) for detailed usage instructions.

### Puppet-lint

Puppet-lint helps ensure that your Puppet code adheres to best practices and style guidelines. To use Puppet-lint, navigate to your Puppet code directory and run:

```bash
$ puppet-lint .

