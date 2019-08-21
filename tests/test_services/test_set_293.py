""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(293)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_293(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables["HostName"] = "auto_host_test4"
    scenario.variables["Password"] = "Z3VhbmxpeXVhbm1pbWExMjMhQCM="
    scenario.variables["ChargeType"] = "Month"
    scenario.variables["CreateCPU"] = 1
    scenario.variables["CreateMem"] = 1024
    scenario.variables["ImageId"] = "#{u_get_image_resource($Region,$Zone)}"
    scenario.variables["BootSize"] = 20
    scenario.variables["BootType"] = "CLOUD_SSD"
    scenario.variables["BootBackup"] = "NONE"
    scenario.variables["DiskSize"] = 20
    scenario.variables["DiskType"] = "CLOUD_NORMAL"
    scenario.variables["DiskBackup"] = "NONE"
    scenario.variables["UHostType"] = "N2"
    scenario.variables["UDiskType"] = "DataDisk"
    scenario.variables["UDiskName"] = "auto_udisk_noArk4"
    scenario.variables["UDataArkMode"] = "No"
    scenario.variables["Size"] = 1

    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDiskPrice",
)
def describe_udisk_price_00(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": variables.get("UDataArkMode"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 1,
        "DiskType": variables.get("UDiskType"),
        "ChargeType": "Month",
    }

    try:
        resp = client.udisk().describe_udisk_price(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CheckUDiskAllowanceResponse"),
    ],
    action="CheckUDiskAllowance",
)
def check_udisk_allowance_01(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Size": 100,
        "Region": variables.get("Region"),
        "Count": 1,
    }

    try:
        resp = client.invoke("CheckUDiskAllowance", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CreateUDiskResponse"),
    ],
    action="CreateUDisk",
)
def create_udisk_02(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": variables.get("UDataArkMode"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 0,
        "Name": variables.get("UDiskName"),
        "DiskType": variables.get("UDiskType"),
        "ChargeType": "Month",
    }

    try:
        resp = client.udisk().create_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["udisk_noArk_id"] = utest.value_at_path(resp, "UDiskId.0")
    return resp


@scenario.step(
    max_retries=5,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_03(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "SetUDiskUDataArkModeResponse"),
    ],
    action="SetUDiskUDataArkMode",
)
def set_udisk__udataark_mode_04(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "UDataArkMode": "Yes",
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().set_udisk__udataark_mode(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=10,
    retry_interval=5,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.UDataArkMode", "Yes"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_05(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=300,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CreateUDiskSnapshotResponse"),
    ],
    action="CreateUDiskSnapshot",
)
def create_udisk_snapshot_06(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
        "Name": "snapshot_01_Ark",
        "Comment": "comment_01_Ark",
    }

    try:
        resp = client.udisk().create_udisk_snapshot(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["snapshot_id"] = utest.value_at_path(resp, "SnapshotId.0")
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=3,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.SnapshotLimit", 3),
        ("str_eq", "DataSet.0.Status", "Available"),
        ("str_eq", "DataSet.0.SnapshotCount", 1),
    ],
    action="DescribeUDisk",
)
def describe_udisk_07(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=20,
    retry_interval=3,
    startup_delay=20,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDiskSnapshotResponse"),
        ("str_eq", "DataSet.0.UDiskId", variables.get("udisk_noArk_id")),
        ("str_eq", "DataSet.0.Status", "Normal"),
    ],
    action="DescribeUDiskSnapshot",
)
def describe_udisk_snapshot_08(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "SnapshotId": variables.get("snapshot_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk_snapshot(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CloneUDiskSnapshotResponse"),
    ],
    action="CloneUDiskSnapshot",
)
def clone_udisk_snapshot_09(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": "Yes",
        "SourceId": variables.get("snapshot_id"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 0,
        "Name": "snap1_clone_Ark",
        "ChargeType": "Month",
    }

    try:
        resp = client.udisk().clone_udisk_snapshot(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["snapClone1_udisk_id"] = utest.value_at_path(resp, "UDiskId.0")
    return resp


@scenario.step(
    max_retries=60,
    retry_interval=5,
    startup_delay=120,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
        ("str_eq", "DataSet.0.Name", "snap1_clone_Ark"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_10(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("snapClone1_udisk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CloneUDiskSnapshot",
)
def clone_udisk_snapshot_11(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": "No",
        "SourceId": variables.get("snapshot_id"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 0,
        "Name": "snap1_clone_noArk",
        "ChargeType": "Month",
    }

    try:
        resp = client.udisk().clone_udisk_snapshot(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["snapClone2_udisk_id"] = utest.value_at_path(resp, "UDiskId.0")
    return resp


@scenario.step(
    max_retries=60,
    retry_interval=5,
    startup_delay=120,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
        ("str_eq", "DataSet.0.Name", "snap1_clone_noArk"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_12(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("snapClone2_udisk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "RestoreUDiskResponse"),
    ],
    action="RestoreUDisk",
)
def restore_udisk_13(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "SnapshotId": variables.get("snapshot_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().restore_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=5,
    retry_interval=1,
    startup_delay=120,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDiskResponse"),
        ("str_eq", "DataSet.0.Status", "Available"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_14(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteSnapshotResponse"),
        ("str_eq", "SnapshotId", variables.get("snapshot_id")),
    ],
    action="DeleteSnapshot",
)
def delete_snapshot_15(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "SnapshotId": variables.get("snapshot_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.invoke("DeleteSnapshot", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=5,
    retry_interval=1,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDiskSnapshotResponse"),
        ("str_eq", "TotalCount", 0),
    ],
    action="DescribeUDiskSnapshot",
)
def describe_udisk_snapshot_16(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "SnapshotId": variables.get("snapshot_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk_snapshot(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=30,
    retry_interval=2,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_17(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteUDiskResponse"),
    ],
    action="DeleteUDisk",
)
def delete_udisk_18(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().delete_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=30,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_19(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("snapClone1_udisk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteUDiskResponse"),
    ],
    action="DeleteUDisk",
)
def delete_udisk_20(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("snapClone1_udisk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().delete_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=30,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_21(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("snapClone2_udisk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=2,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteUDiskResponse"),
    ],
    action="DeleteUDisk",
)
def delete_udisk_22(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("snapClone2_udisk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().delete_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
