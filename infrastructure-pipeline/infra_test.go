package test

import (
	"testing"
	"://github.com"
	"://github.com"
)

func TestSecurityGroupRules(t *testing.T) {
	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		TerraformDir: "../",
	})

	// Clean up infrastructure at the end of the test execution
	defer terraform.Destroy(t, terraformOptions)

	// Deploy infrastructure
	terraform.InitAndApply(t, terraformOptions)

	// Fetch variables/outputs from deployed environment
	sgIngressRules := terraform.OutputList(t, terraformOptions, "security_group_ingress")

	// Programmatic assertion verifying network safety requirements are met
	for _, rule := range sgIngressRules {
		if rule["from_port"] == "22" {
			assert.NotContains(t, rule["cidr_blocks"], "0.0.0.0/0", "Security Vulnerability: Port 22 is open to the public internet!")
		}
	}
}
