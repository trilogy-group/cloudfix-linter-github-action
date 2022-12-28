import json
import getopt, sys
import uuid
import traceback
import platform

argumentList = sys.argv[1:]

def generate_volume_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "region": region,
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "staging",
        "annualSavings": 33.15,
        "annualCost": 419.51,
        "status": "Manual Approval",
        "parameters": {},
        "templateApproved": False,
        "customerId": 5,
        "accountId": "631108317415",
        "accountNickname": "cloudfixtf-linter-demo",
        "opportunityType": "Gp2Gp3",
        "opportunityDescription": "EBS GP2 to Gp3",
        "generatedDate": "2022-06-20T07:01:17.274Z",
        "lastUpdatedDate": "2022-06-20T07:01:17.274Z"
    }

def generate_intel_to_amd_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "region": region,
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "staging",
        "annualSavings": 57.31,
        "annualCost": 596.00,
        "status": "Manual Approval",
        "parameters": {
            "Migrating to instance type": "t3a.micro",
            "Has recent snapshot": True
        },
        "templateApproved": True,
        "customerId": 5,
        "accountId": account,
        "accountNickname": "cloudfixtf-linter-demo",
        "opportunityType": "Ec2IntelToAmd",
        "opportunityDescription": "EC2 Intel to AMD",
        "generatedDate": "2022-05-06T12:10:11.568Z",
        "lastUpdatedDate": "2022-06-20T07:01:21.847Z"
    }

def generate_s3_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "region": region,
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "staging",
        "annualSavings": 33.15,
        "annualCost": 419.51,
        "status": "Manual Approval",
        "parameters": {},
        "templateApproved": False,
        "customerId": 5,
        "accountId": account,
        "accountNickname": "cloudfixtf-linter-demo",
        "opportunityType": "StandardToSIT",
        "opportunityDescription": "Intelligent Tiering for S3",
        "generatedDate": "2022-06-20T07:01:17.274Z",
        "lastUpdatedDate": "2022-06-20T07:01:17.274Z"
    }

def generate_efs_ia_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "region": region,
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "staging",
        "annualSavings": 33.15,
        "annualCost": 419.51,
        "status": "Manual Approval",
        "parameters": {},
        "templateApproved": False,
        "customerId": 5,
        "accountId": account,
        "accountNickname": "cloudfixtf-linter-demo",
        "opportunityType": "EfsInfrequentAccess",
        "opportunityDescription": "Intelligent Tiering for EFS",
        "generatedDate": "2022-06-20T07:01:17.274Z",
        "lastUpdatedDate": "2022-06-20T07:01:17.274Z"
    }

def generate_io_to_gp3_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "754692398214",
        "accountNickname": "Acorn",
        "opportunityType": "IoToGp3",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "EBS IO1/IO2 to Gp3",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 2632.49,
        "annualCost": 3171.68,
        "actualSavings": 3003.88,
        "changeRequestId": "oi-f890262dde18",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-10-23T01:02:53.000Z",
        "updatedAt": "2022-10-23T06:24:13.000Z",
        "status": "Completed",
        "scheduledAt": "2022-10-23T06:05:56.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_unused_ebs_volume_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "887704487240",
        "accountNickname": "CentralNetwork",
        "opportunityType": "UnusedEBSVolumes",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Restricted Area",
        "opportunityDescription": "Cleanup unattached EBS Volumes.",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 353.75,
        "annualCost": 786.12,
        "actualSavings": None,
        "changeRequestId": "oi-f11759c12269",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-10-26T09:08:06.000Z",
        "updatedAt": "2022-10-27T08:07:17.000Z",
        "status": "Completed",
        "scheduledAt": "2022-10-27T08:06:16.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_vpc_idle_endpoint_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "082830052325",
        "accountNickname": "CodenationProd",
        "opportunityType": "VpcIdleEndpoint",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Production",
        "opportunityDescription": "Cleanup Idle VPC Endpoints",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 2,
        "risk": 2,
        "applicationEnvironment": "prod",
        "annualSavings": 153.92,
        "annualCost": 153.92,
        "actualSavings": 153.92,
        "changeRequestId": "oi-01c43e7f84f8",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-11-10T22:37:27.000Z",
        "updatedAt": "2022-11-15T03:41:59.000Z",
        "status": "Completed",
        "scheduledAt": "2022-11-15T03:41:07.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_cloudtrail_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "529493049876",
        "accountNickname": "InsideSales Atom",
        "opportunityType": "DuplicateCloudTrail",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Prod",
        "opportunityDescription": "Disable duplicate CloudTrails",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 130.74,
        "annualCost": 130.74,
        "actualSavings": None,
        "changeRequestId": "oi-cff1aa024121",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-11-29T04:40:50.000Z",
        "updatedAt": "2022-12-01T04:19:41.000Z",
        "status": "Completed",
        "scheduledAt": "2022-12-01T04:19:16.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }
def generate_efs_intelli_tiering_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": account,
        "accountNickname": "Prod-Think3-SLIVMWARE",
        "opportunityType": "EfsIntelligentTiering",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Prod",
        "opportunityDescription": "EFS Intelligent Tiering",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": "arn:aws:elasticfilesystem:us-east-1:610092376560:file-system/fs-e6142b52",
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 5520.7,
        "annualCost": 11041.4,
        "actualSavings": None,
        "changeRequestId": "oi-6abcb5466180",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-07-25T07:01:33.000Z",
        "updatedAt": "2022-10-17T03:03:44.000Z",
        "status": "Completed",
        "scheduledAt": "2022-10-17T03:01:32.000Z",
        "parameters": {},
        "isTemplateApproved": False,
        "autoApproved": True,
        "isTemplateAvailable": True,
        "approverLink": "https://signin.aws.amazon.com/switchrole?account=610092376560&roleName=cloudfix-fixer-approver-role&displayName=TemplateApproval&redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fsystems-manager%2Fchange-manager%3Fregion%3Dus-east-1%23%2Fchange-template%2Fview-details%2FCloudfix-Template-EfsIntelligentTiering-prod%2Fdetails"
    }

def generate_neptune_idle_cluster_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": account,
        "accountNickname": "Dev-DevFactory-TIQ32022",
        "opportunityType": "NeptuneCleanupIdleClusters",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non-prod",
        "opportunityDescription": "Cleanup Idle Neptune Clusters",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 1489.24,
        "annualCost": 1654.71,
        "actualSavings": None,
        "changeRequestId": "oi-994a09b59ddb",
        "changeRequestStatus": "CompletedWithFailure",
        "createdAt": "2022-12-02T21:56:44.000Z",
        "updatedAt": "2022-12-04T02:59:44.000Z",
        "status": "Failed",
        "scheduledAt": "2022-12-04T02:58:44.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_dynamo_db_provisioning_reco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": account,
        "accountNickname": "jive-microservices-prod",
        "opportunityType": "DynamoDbProvisioning",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Prod",
        "opportunityDescription": "DynamoDB Use Provisioning and Autoscaling",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 2,
        "risk": 2,
        "applicationEnvironment": "prod",
        "annualSavings": 89.96,
        "annualCost": 105.41,
        "actualSavings": None,
        "changeRequestId": "oi-0b2897dfe9fc",
        "changeRequestStatus": "CompletedWithFailure",
        "createdAt": "2022-12-01T03:27:18.000Z",
        "updatedAt": "2022-12-05T03:21:59.000Z",
        "status": "Failed",
        "scheduledAt": "2022-12-05T03:20:48.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_install_ssm_agent_windows_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "042966178169",
        "accountNickname": "Jive PS Sandbox",
        "opportunityType": "InstallSSMAgentWindows",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non-prod",
        "opportunityDescription": "InstallSSMAgentWindows",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 2,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 560.59,
        "actualSavings": None,
        "changeRequestId": "oi-f2142ba50a30",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-12-02T20:49:28.000Z",
        "updatedAt": "2022-12-05T03:15:04.000Z",
        "status": "Scheduled",
        "scheduledAt": "2022-12-05T03:16:00.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_install_ssm_agent_mac_linux_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "517449413234",
        "accountNickname": "jive-infra-pipeline",
        "opportunityType": "InstallSSMAgentLinuxMacSSH",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non-prod",
        "opportunityDescription": "Installs SSM agent for Mac and Linux via SSH",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 2,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 178.05,
        "actualSavings": None,
        "changeRequestId": "oi-3212adae9b73",
        "changeRequestStatus": "CompletedWithFailure",
        "createdAt": "2022-11-21T03:54:44.000Z",
        "updatedAt": "2022-11-26T03:57:14.000Z",
        "status": "Failed",
        "scheduledAt": "2022-11-24T03:40:53.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_vpc_nat_gateway_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "082830052325",
        "accountNickname": "CodenationProd",
        "opportunityType": "VpcIdleNatGateway",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Production",
        "opportunityDescription": "VPC Cleanup Idle NAT Gateways",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 2,
        "risk": 2,
        "applicationEnvironment": "prod",
        "annualSavings": 339.8,
        "annualCost": 339.8,
        "actualSavings": 339.8,
        "changeRequestId": "oi-efbe25c2d1e7",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-10-30T07:01:50.000Z",
        "updatedAt": "2022-11-07T06:13:29.000Z",
        "status": "Completed",
        "scheduledAt": "2022-11-07T06:12:45.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_vpc_dns_agents_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "104075470635",
        "accountNickname": "NewNet",
        "opportunityType": "FixVPCDNSForAgents",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non-prod",
        "opportunityDescription": "FixVPCDNSForAgents",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 2,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 0,
        "actualSavings": None,
        "changeRequestId": "oi-e6ee6aa4f46f",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-11-28T00:21:01.000Z",
        "updatedAt": "2022-11-29T00:13:08.000Z",
        "status": "Failed",
        "scheduledAt": "2022-11-29T00:14:05.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_es_optimize_storage_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "517449413234",
        "accountNickname": "jive-infra-pipeline",
        "opportunityType": "EsOptimizeStorage",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non-prod",
        "opportunityDescription": "Shrink AWS OpenSearch volumes",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 2,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 516,
        "annualCost": 699.49,
        "actualSavings": None,
        "changeRequestId": "oi-b29476e7b71e",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-11-14T20:48:55.000Z",
        "updatedAt": "2022-11-16T03:42:52.000Z",
        "status": "Failed",
        "scheduledAt": "2022-11-16T03:43:49.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_s3_ddb_traffic_to_gw_end_point_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "646253092271",
        "accountNickname": "Central",
        "opportunityType": "S3DDBTrafficToGWEndpoint",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Restricted Area",
        "opportunityDescription": "S3/DynamoDB Traffic to Gateway Endpoint",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 2,
        "applicationEnvironment": "prod",
        "annualSavings": 2872.03,
        "annualCost": 2872.03,
        "actualSavings": None,
        "changeRequestId": "oi-0e8612c4fe52",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-12-02T20:49:37.000Z",
        "updatedAt": "2022-12-04T02:57:41.000Z",
        "status": "Completed",
        "scheduledAt": "2022-12-04T02:57:22.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_ec2_low_risk_right_size_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "529464811624",
        "accountNickname": "NS8",
        "opportunityType": "Ec2LowRiskRightsize",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Prod",
        "opportunityDescription": "Ec2LowRiskRightsize",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 3,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 68.58,
        "annualCost": 137.16,
        "actualSavings": 92.3,
        "changeRequestId": "oi-50ad98ce33b9",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-11-28T00:21:16.000Z",
        "updatedAt": "2022-11-29T04:51:07.000Z",
        "status": "Completed",
        "scheduledAt": "2022-11-29T04:42:23.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_archive_old_ebs_volume_snapshot_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "724994046559",
        "accountNickname": "Dev-Think3-Agemni",
        "opportunityType": "ArchiveOldEbsVolumeSnapshots",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "Archive old EBS volume snapshots.",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 90.74,
        "annualCost": 92,
        "actualSavings": None,
        "changeRequestId": "oi-55346e1a0082",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-12-04T01:05:11.000Z",
        "updatedAt": "2022-12-05T03:19:41.000Z",
        "status": "Completed",
        "scheduledAt": "2022-12-05T03:19:36.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_dynamo_db_infrequent_access_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "646253092271",
        "accountNickname": "Central",
        "opportunityType": "DynamoDbInfrequentAccess",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Restricted Area",
        "opportunityDescription": "DynamoDB Infrequent Access",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 123.08,
        "annualCost": 421.73,
        "actualSavings": 239.41,
        "changeRequestId": "oi-1a92de9980b8",
        "changeRequestStatus": "CompletedWithSuccess",
        "createdAt": "2022-08-09T13:36:21.000Z",
        "updatedAt": "2022-10-17T03:44:45.000Z",
        "status": "Completed",
        "scheduledAt": "2022-10-17T03:43:55.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_instance_profile_for_agents_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "179862436593",
        "accountNickname": "Dev-AureaEnterprise-InsideSales",
        "opportunityType": "FixInstanceProfileForAgents",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "FixInstanceProfileForAgents",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 39.27,
        "actualSavings": None,
        "changeRequestId": "oi-5605be09af3d",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-12-02T20:50:38.000Z",
        "updatedAt": "2022-12-05T03:35:31.000Z",
        "status": "Scheduled",
        "scheduledAt": "2022-12-05T03:36:28.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_es_graviton_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "438051315841",
        "accountNickname": "Dev-CentralFunctions-CostOptimization",
        "opportunityType": "Es79Graviton",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "CloudFix-Dev",
        "opportunityDescription": "Elasticsearch to Graviton",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 123,
        "annualCost": 119.14,
        "actualSavings": None,
        "changeRequestId": "oi-2348113c4bc1",
        "changeRequestStatus": "CompletedWithFailure",
        "createdAt": "2022-12-04T01:04:17.000Z",
        "updatedAt": "2022-12-05T03:37:12.000Z",
        "status": "Failed",
        "scheduledAt": "2022-12-05T03:35:54.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": True,
        "isTemplateAvailable": True
    }

def generate_cloudfront_compression_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "179862436593",
        "accountNickname": "Dev-AureaEnterprise-InsideSales",
        "opportunityType": "CloudFrontCompression",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "CloudFrontCompression",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 39.27,
        "actualSavings": None,
        "changeRequestId": "oi-5605be09af3d",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-12-02T20:50:38.000Z",
        "updatedAt": "2022-12-05T03:35:31.000Z",
        "status": "Scheduled",
        "scheduledAt": "2022-12-05T03:36:28.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_elb_cleanup_idle_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "179862436593",
        "accountNickname": "Dev-AureaEnterprise-InsideSales",
        "opportunityType": "ElbCleanUpIdle",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "ElbCleanUpIdle",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 39.27,
        "actualSavings": None,
        "changeRequestId": "oi-5605be09af3d",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-12-02T20:50:38.000Z",
        "updatedAt": "2022-12-05T03:35:31.000Z",
        "status": "Scheduled",
        "scheduledAt": "2022-12-05T03:36:28.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_ec2_cleanup_unused_amis_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "179862436593",
        "accountNickname": "Dev-AureaEnterprise-InsideSales",
        "opportunityType": "EC2CleanupUnusedAMIs",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "EC2CleanupUnusedAMIs",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 39.27,
        "actualSavings": None,
        "changeRequestId": "oi-5605be09af3d",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-12-02T20:50:38.000Z",
        "updatedAt": "2022-12-05T03:35:31.000Z",
        "status": "Scheduled",
        "scheduledAt": "2022-12-05T03:36:28.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_opensearch_right_size_clusters_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "179862436593",
        "accountNickname": "Dev-AureaEnterprise-InsideSales",
        "opportunityType": "OpenSearchRightSizeClusters",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "OpenSearchRightSizeClusters",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 39.27,
        "actualSavings": None,
        "changeRequestId": "oi-5605be09af3d",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-12-02T20:50:38.000Z",
        "updatedAt": "2022-12-05T03:35:31.000Z",
        "status": "Scheduled",
        "scheduledAt": "2022-12-05T03:36:28.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_rds_right_size_mysql_clusters_recco(region, account, resource_id, resource_name):
    return {
        "id": str(uuid.uuid4()),
        "customerId": 10002,
        "accountId": "179862436593",
        "accountNickname": "Dev-AureaEnterprise-InsideSales",
        "opportunityType": "RDSRightSizeMySqlClusters",
        "opportunityId": "",
        "region": region,
        "organizationalUnitName": "Non Production",
        "opportunityDescription": "RDSRightSizeMySqlClusters",
        "primaryImpactedNodeId": resource_id,
        "otherImpactedNodeIds": [],
        "resourceId": resource_id,
        "resourceName": resource_name,
        "difficulty": 1,
        "risk": 1,
        "applicationEnvironment": "prod",
        "annualSavings": 0,
        "annualCost": 39.27,
        "actualSavings": None,
        "changeRequestId": "oi-5605be09af3d",
        "changeRequestStatus": "Failed",
        "createdAt": "2022-12-02T20:50:38.000Z",
        "updatedAt": "2022-12-05T03:35:31.000Z",
        "status": "Scheduled",
        "scheduledAt": "2022-12-05T03:36:28.000Z",
        "parameters": {},
        "isTemplateApproved": True,
        "autoApproved": False,
        "isTemplateAvailable": True
    }

def generate_recos(item):
    if item['type'] == 'aws_ebs_volume':
        return [generate_volume_reco(region, account_id, item['values']['id'], item['name']),
        # generate_io_to_gp3_reco(region, account_id, item['values']['id'], item['name']),
        generate_unused_ebs_volume_reco(region, account_id, item['values']['id'], item['name']),
        generate_archive_old_ebs_volume_snapshot_recco(region, account_id, item['values']['id'], item['name']),
        ]

    if item['type'] == 'aws_instance':
        return [generate_intel_to_amd_reco(region, account_id, item['values']['id'], item['name']),
        generate_install_ssm_agent_mac_linux_recco(region, account_id, item['values']['id'], item['name']),
        generate_install_ssm_agent_windows_recco(region, account_id, item['values']['id'], item['name']),
        # generate_ec2_low_risk_right_size_recco(region, account_id, item['values']['id'], item['name'])
        ]

    if item['type'] == 'aws_ami':
        return [generate_ec2_cleanup_unused_amis_recco(region, account_id, item['values']['id'], item['name'])]

    if item['type'] == 'aws_s3_bucket':
        return [generate_s3_reco(region, account_id, item['values']['bucket'], item['values']['bucket'])]

    if item['type'] == 'aws_efs_file_system':
        return [generate_efs_ia_reco(region, account_id, item['values']['id'], item['name']),
        generate_efs_intelli_tiering_recco(region, account_id, item['values']['id'], item['name'])
        ]
    if item['type'] == 'aws_neptune_cluster':
        return [generate_neptune_idle_cluster_reco(region, account_id, item['values']['id'], item['name'])]
        
    if item['type'] == 'aws_vpc_endpoint':
        return [generate_vpc_idle_endpoint_recco(region, account_id, item['values']['id'], item['name'])]

    if item['type'] == 'aws_dynamodb_table':
        return [
            # generate_dynamo_db_infrequent_access_recco(region, account_id, item['values']['id'], item['name']),
            generate_dynamo_db_provisioning_reco(region, account_id, item['values']['id'], item['name'])
        ]

    if item['type'] == 'aws_cloudtrail':
        return [generate_cloudtrail_recco(region, account_id, item['values']['id'], item['name'])]

    if item['type'] == 'aws_nat_gateway':
        return [generate_vpc_nat_gateway_recco(region, account_id, item['values']['id'], item['name']),
        generate_s3_ddb_traffic_to_gw_end_point_recco(region, account_id, item['values']['id'], item['name'])
        ]

    if item['type'] == 'aws_opensearch_domain':
        return [generate_es_optimize_storage_recco(region, account_id, item['values']['id'], item['name']),
        # generate_es_graviton_recco(region, account_id, item['values']['id'], item['name']),
        # generate_opensearch_right_size_clusters_recco(region, account_id, item['values']['id'], item['name'])
        ]

    # if item['type'] == 'aws_rds_cluster':
    #     return [generate_rds_right_size_mysql_clusters_recco(region, account_id, item['values']['id'], item['name'])]

    if item['type'] == 'aws_elb':
        return [generate_elb_cleanup_idle_recco(region, account_id, item['values']['id'], item['name'])]

    if item['type'] == 'aws_cloudfront_distribution':
        return [generate_cloudfront_compression_recco(region, account_id, item['values']['id'], item['name'])]

try:
    if platform.system()=="Windows":
        tf = open(sys.argv[1],encoding="utf-16").read()
        data = json.loads(tf)
    else:
        tf = open(sys.argv[1]).read()
        print(platform.system())
        print(tf)
        data = json.loads(tf)
    arn = data['values']['root_module']['resources'][0]['values']['arn']
    
    account_id = arn.split(":")[4]
    region = arn.split(":")[3]
    recos = []
    with open("./reccos.json","w") as reco:
        for item in data['values']['root_module']['resources']:
            r = generate_recos(item)
            if r!=None:
                recos.extend(r)
        reco.write(json.dumps(recos))
except Exception as e:
    traceback.print_exc()
    
