# B2368Update

A basic API to bypass the update lock in a Huawei B2368 router that is deployed to AWS using the [chalice](https://aws.github.io/chalice/) microframework.

## Prerequisites

Install chalice with

```
pip3 install chalice
```

## Deployment

Run

```bash
cd b2368-update-lambda
chalice deploy
```

## Usage

Replace the `http://query.hicloud.com/cpe_and_common/v2/Check.action?latest=true` URL in **Online Upgrade** section of the router administration portal using the **Inspect Element** tool of your browser with the URL of the lambda function returned by the `deploy` command.
