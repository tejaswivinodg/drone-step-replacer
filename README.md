# Drone-Step-Replacer

This binary will replace `deploy_to_kubernetes_qa_manual` step's conditional to enable Git branch deployment workflow.
More info about Git branch deployment workflow is in [RFC](https://go/rfc/qa-deploy-strategy) and [documentation](https://wiki.squarespace.net/pages/viewpage.action?pageId=123836169).

## Usage:

1. Use `replacer make-changes <drone_file_path>` to make changes in drone file to enable Git branch deployment.
2. Use `replacer verify-changes <drone_file_path>` to show changes made in drone file.
3. Use `replacer create-pr` to create PR with Drone config changes.
