# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('service_mesh.service_mesh_root_group.command_name', 'service-mesh'), cls=CommandGroupWithAlias, help=cli_util.override('service_mesh.service_mesh_root_group.help', """Use the Service Mesh API to manage mesh, virtual service, access policy and other mesh related items."""), short_help=cli_util.override('service_mesh.service_mesh_root_group.short_help', """Service Mesh API"""))
@cli_util.help_option_group
def service_mesh_root_group():
    pass


@click.command(cli_util.override('service_mesh.virtual_deployment_group.command_name', 'virtual-deployment'), cls=CommandGroupWithAlias, help="""This resource represents a customer-managed virtual service deployment in the Service Mesh.""")
@cli_util.help_option_group
def virtual_deployment_group():
    pass


@click.command(cli_util.override('service_mesh.ingress_gateway_route_table_group.command_name', 'ingress-gateway-route-table'), cls=CommandGroupWithAlias, help="""This resource represents a customer-managed ingress gateway route table in the Service Mesh.""")
@cli_util.help_option_group
def ingress_gateway_route_table_group():
    pass


@click.command(cli_util.override('service_mesh.ingress_gateway_group.command_name', 'ingress-gateway'), cls=CommandGroupWithAlias, help="""An ingress gateway allows resources that are outside of a mesh to communicate to resources that are inside the mesh. It sits on the edge of a service mesh receiving incoming HTTP/TCP connections to the mesh.""")
@cli_util.help_option_group
def ingress_gateway_group():
    pass


@click.command(cli_util.override('service_mesh.proxy_details_group.command_name', 'proxy-details'), cls=CommandGroupWithAlias, help="""Details of the proxy such as version of the proxy image.""")
@cli_util.help_option_group
def proxy_details_group():
    pass


@click.command(cli_util.override('service_mesh.access_policy_group.command_name', 'access-policy'), cls=CommandGroupWithAlias, help="""Access policies enable administrators to restrict the access of certain services.""")
@cli_util.help_option_group
def access_policy_group():
    pass


@click.command(cli_util.override('service_mesh.virtual_service_route_table_group.command_name', 'virtual-service-route-table'), cls=CommandGroupWithAlias, help="""This resource represents a customer-managed service route table in the Service Mesh.""")
@cli_util.help_option_group
def virtual_service_route_table_group():
    pass


@click.command(cli_util.override('service_mesh.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of the work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('service_mesh.mesh_group.command_name', 'mesh'), cls=CommandGroupWithAlias, help="""The mesh resource is the top-level container that represents the logical boundary of application traffic between the services and deployments that reside within it. A mesh also provides a unit of access control.""")
@cli_util.help_option_group
def mesh_group():
    pass


@click.command(cli_util.override('service_mesh.virtual_service_group.command_name', 'virtual-service'), cls=CommandGroupWithAlias, help="""This resource represents a customer-managed service in the Service Mesh. Each virtual service declares multiple running versions of the service and maps to a group of instances/pods running a specific version of the actual service.""")
@cli_util.help_option_group
def virtual_service_group():
    pass


service_mesh_root_group.add_command(virtual_deployment_group)
service_mesh_root_group.add_command(ingress_gateway_route_table_group)
service_mesh_root_group.add_command(ingress_gateway_group)
service_mesh_root_group.add_command(proxy_details_group)
service_mesh_root_group.add_command(access_policy_group)
service_mesh_root_group.add_command(virtual_service_route_table_group)
service_mesh_root_group.add_command(work_request_group)
service_mesh_root_group.add_command(mesh_group)
service_mesh_root_group.add_command(virtual_service_group)


@work_request_group.command(name=cli_util.override('service_mesh.cancel_work_request.command_name', 'cancel'), help=u"""Cancels the work request with the given ID. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_policy_group.command(name=cli_util.override('service_mesh.change_access_policy_compartment.command_name', 'change-compartment'), help=u"""Moves an AccessPolicy resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeAccessPolicyCompartment)""")
@cli_util.option('--access-policy-id', required=True, help=u"""Unique AccessPolicy identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_access_policy_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, access_policy_id, compartment_id, if_match):

    if isinstance(access_policy_id, six.string_types) and len(access_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --access-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.change_access_policy_compartment(
        access_policy_id=access_policy_id,
        change_access_policy_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_group.command(name=cli_util.override('service_mesh.change_ingress_gateway_compartment.command_name', 'change-compartment'), help=u"""Moves a IngressGateway resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeIngressGatewayCompartment)""")
@cli_util.option('--ingress-gateway-id', required=True, help=u"""Unique IngressGateway identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ingress_gateway_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ingress_gateway_id, compartment_id, if_match):

    if isinstance(ingress_gateway_id, six.string_types) and len(ingress_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.change_ingress_gateway_compartment(
        ingress_gateway_id=ingress_gateway_id,
        change_ingress_gateway_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_route_table_group.command(name=cli_util.override('service_mesh.change_ingress_gateway_route_table_compartment.command_name', 'change-compartment'), help=u"""Moves a IngressGatewayRouteTable resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeIngressGatewayRouteTableCompartment)""")
@cli_util.option('--ingress-gateway-route-table-id', required=True, help=u"""Unique IngressGatewayRouteTable identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ingress_gateway_route_table_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ingress_gateway_route_table_id, compartment_id, if_match):

    if isinstance(ingress_gateway_route_table_id, six.string_types) and len(ingress_gateway_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.change_ingress_gateway_route_table_compartment(
        ingress_gateway_route_table_id=ingress_gateway_route_table_id,
        change_ingress_gateway_route_table_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mesh_group.command(name=cli_util.override('service_mesh.change_mesh_compartment.command_name', 'change-compartment'), help=u"""Moves a Mesh resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeMeshCompartment)""")
@cli_util.option('--mesh-id', required=True, help=u"""Unique Mesh identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_mesh_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, mesh_id, compartment_id, if_match):

    if isinstance(mesh_id, six.string_types) and len(mesh_id.strip()) == 0:
        raise click.UsageError('Parameter --mesh-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.change_mesh_compartment(
        mesh_id=mesh_id,
        change_mesh_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.change_virtual_deployment_compartment.command_name', 'change-compartment'), help=u"""Moves a VirtualDeployment resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeVirtualDeploymentCompartment)""")
@cli_util.option('--virtual-deployment-id', required=True, help=u"""Unique VirtualDeployment identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_virtual_deployment_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_deployment_id, compartment_id, if_match):

    if isinstance(virtual_deployment_id, six.string_types) and len(virtual_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.change_virtual_deployment_compartment(
        virtual_deployment_id=virtual_deployment_id,
        change_virtual_deployment_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_group.command(name=cli_util.override('service_mesh.change_virtual_service_compartment.command_name', 'change-compartment'), help=u"""Moves a VirtualService resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeVirtualServiceCompartment)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""Unique VirtualService identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_virtual_service_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_id, compartment_id, if_match):

    if isinstance(virtual_service_id, six.string_types) and len(virtual_service_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.change_virtual_service_compartment(
        virtual_service_id=virtual_service_id,
        change_virtual_service_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_route_table_group.command(name=cli_util.override('service_mesh.change_virtual_service_route_table_compartment.command_name', 'change-compartment'), help=u"""Moves a VirtualServiceRouteTable resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeVirtualServiceRouteTableCompartment)""")
@cli_util.option('--virtual-service-route-table-id', required=True, help=u"""Unique VirtualServiceRouteTable identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_virtual_service_route_table_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_route_table_id, compartment_id, if_match):

    if isinstance(virtual_service_route_table_id, six.string_types) and len(virtual_service_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.change_virtual_service_route_table_compartment(
        virtual_service_route_table_id=virtual_service_route_table_id,
        change_virtual_service_route_table_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@access_policy_group.command(name=cli_util.override('service_mesh.create_access_policy.command_name', 'create'), help=u"""Creates a new AccessPolicy. \n[Command Reference](createAccessPolicy)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--mesh-id', required=True, help=u"""The OCID of the service mesh in which this access policy is created.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of applicable rules""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'rules': {'module': 'service_mesh', 'class': 'list[AccessPolicyRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'rules': {'module': 'service_mesh', 'class': 'list[AccessPolicyRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'AccessPolicy'})
@cli_util.wrap_exceptions
def create_access_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, mesh_id, compartment_id, rules, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['meshId'] = mesh_id
    _details['compartmentId'] = compartment_id
    _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_access_policy(
        create_access_policy_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_group.command(name=cli_util.override('service_mesh.create_ingress_gateway.command_name', 'create'), help=u"""Creates a new IngressGateway. \n[Command Reference](createIngressGateway)""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--mesh-id', required=True, help=u"""The OCID of the service mesh in which this ingress gateway is created.""")
@cli_util.option('--hosts', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of hostnames and their listener configuration that this gateway will bind to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--mtls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'hosts': {'module': 'service_mesh', 'class': 'list[IngressGatewayHost]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'mtls': {'module': 'service_mesh', 'class': 'IngressGatewayMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hosts': {'module': 'service_mesh', 'class': 'list[IngressGatewayHost]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'mtls': {'module': 'service_mesh', 'class': 'IngressGatewayMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'IngressGateway'})
@cli_util.wrap_exceptions
def create_ingress_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, mesh_id, hosts, compartment_id, description, access_logging, mtls, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['meshId'] = mesh_id
    _details['hosts'] = cli_util.parse_json_parameter("hosts", hosts)
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if mtls is not None:
        _details['mtls'] = cli_util.parse_json_parameter("mtls", mtls)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_ingress_gateway(
        create_ingress_gateway_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_route_table_group.command(name=cli_util.override('service_mesh.create_ingress_gateway_route_table.command_name', 'create'), help=u"""Creates a new IngressGatewayRouteTable. \n[Command Reference](createIngressGatewayRouteTable)""")
@cli_util.option('--ingress-gateway-id', required=True, help=u"""The OCID of the service mesh in which this access policy is created.""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--route-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The route rules for the ingress gateway.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--priority', type=click.INT, help=u"""The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'route-rules': {'module': 'service_mesh', 'class': 'list[IngressGatewayTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'route-rules': {'module': 'service_mesh', 'class': 'list[IngressGatewayTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'IngressGatewayRouteTable'})
@cli_util.wrap_exceptions
def create_ingress_gateway_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ingress_gateway_id, name, route_rules, compartment_id, description, priority, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['ingressGatewayId'] = ingress_gateway_id
    _details['name'] = name
    _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if priority is not None:
        _details['priority'] = priority

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_ingress_gateway_route_table(
        create_ingress_gateway_route_table_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mesh_group.command(name=cli_util.override('service_mesh.create_mesh.command_name', 'create'), help=u"""Creates a new Mesh. \n[Command Reference](createMesh)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. The name does not have to be unique and can be changed after creation. Avoid entering confidential information.

Example: `My new resource`""")
@cli_util.option('--certificate-authorities', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCID of the certificate authority resource OCID to use for creating leaf certificates.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--mtls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'certificate-authorities': {'module': 'service_mesh', 'class': 'list[CertificateAuthority]'}, 'mtls': {'module': 'service_mesh', 'class': 'MeshMutualTransportLayerSecurity'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-authorities': {'module': 'service_mesh', 'class': 'list[CertificateAuthority]'}, 'mtls': {'module': 'service_mesh', 'class': 'MeshMutualTransportLayerSecurity'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'Mesh'})
@cli_util.wrap_exceptions
def create_mesh(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, certificate_authorities, compartment_id, description, mtls, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['certificateAuthorities'] = cli_util.parse_json_parameter("certificate_authorities", certificate_authorities)
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if mtls is not None:
        _details['mtls'] = cli_util.parse_json_parameter("mtls", mtls)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_mesh(
        create_mesh_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.create_virtual_deployment.command_name', 'create'), help=u"""Creates a new VirtualDeployment. \n[Command Reference](createVirtualDeployment)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""The OCID of the service mesh in which this access policy is created.""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--service-discovery', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The listeners for the virtual deployment.

This option is a JSON list with items of type VirtualDeploymentListener.  For documentation on VirtualDeploymentListener please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/VirtualDeploymentListener.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-discovery': {'module': 'service_mesh', 'class': 'ServiceDiscoveryConfiguration'}, 'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-discovery': {'module': 'service_mesh', 'class': 'ServiceDiscoveryConfiguration'}, 'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'VirtualDeployment'})
@cli_util.wrap_exceptions
def create_virtual_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_id, name, compartment_id, description, service_discovery, listeners, access_logging, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['virtualServiceId'] = virtual_service_id
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if service_discovery is not None:
        _details['serviceDiscovery'] = cli_util.parse_json_parameter("service_discovery", service_discovery)

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_virtual_deployment(
        create_virtual_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.create_virtual_deployment_dns_service_discovery_configuration.command_name', 'create-virtual-deployment-dns-service-discovery-configuration'), help=u"""Creates a new VirtualDeployment. \n[Command Reference](createVirtualDeployment)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""The OCID of the service mesh in which this access policy is created.""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--service-discovery-hostname', required=True, help=u"""The hostname of the virtual deployments.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The listeners for the virtual deployment.

This option is a JSON list with items of type VirtualDeploymentListener.  For documentation on VirtualDeploymentListener please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/VirtualDeploymentListener.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'VirtualDeployment'})
@cli_util.wrap_exceptions
def create_virtual_deployment_dns_service_discovery_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_id, name, compartment_id, service_discovery_hostname, description, listeners, access_logging, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceDiscovery'] = {}
    _details['virtualServiceId'] = virtual_service_id
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['serviceDiscovery']['hostname'] = service_discovery_hostname

    if description is not None:
        _details['description'] = description

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['serviceDiscovery']['type'] = 'DNS'

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_virtual_deployment(
        create_virtual_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.create_virtual_deployment_disabled_service_discovery_configuration.command_name', 'create-virtual-deployment-disabled-service-discovery-configuration'), help=u"""Creates a new VirtualDeployment. \n[Command Reference](createVirtualDeployment)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""The OCID of the service mesh in which this access policy is created.""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The listeners for the virtual deployment.

This option is a JSON list with items of type VirtualDeploymentListener.  For documentation on VirtualDeploymentListener please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/VirtualDeploymentListener.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'VirtualDeployment'})
@cli_util.wrap_exceptions
def create_virtual_deployment_disabled_service_discovery_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_id, name, compartment_id, description, listeners, access_logging, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceDiscovery'] = {}
    _details['virtualServiceId'] = virtual_service_id
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['serviceDiscovery']['type'] = 'DISABLED'

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_virtual_deployment(
        create_virtual_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_group.command(name=cli_util.override('service_mesh.create_virtual_service.command_name', 'create'), help=u"""Creates a new VirtualService. \n[Command Reference](createVirtualService)""")
@cli_util.option('--mesh-id', required=True, help=u"""The OCID of the service mesh in which this virtual service is created.""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--default-routing-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hosts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The DNS hostnames of the virtual service that is used by its callers. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\". Can be omitted if the virtual service will only have TCP virtual deployments.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--mtls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'default-routing-policy': {'module': 'service_mesh', 'class': 'DefaultVirtualServiceRoutingPolicy'}, 'hosts': {'module': 'service_mesh', 'class': 'list[string]'}, 'mtls': {'module': 'service_mesh', 'class': 'VirtualServiceMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'default-routing-policy': {'module': 'service_mesh', 'class': 'DefaultVirtualServiceRoutingPolicy'}, 'hosts': {'module': 'service_mesh', 'class': 'list[string]'}, 'mtls': {'module': 'service_mesh', 'class': 'VirtualServiceMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'VirtualService'})
@cli_util.wrap_exceptions
def create_virtual_service(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, mesh_id, name, compartment_id, description, default_routing_policy, hosts, mtls, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['meshId'] = mesh_id
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if default_routing_policy is not None:
        _details['defaultRoutingPolicy'] = cli_util.parse_json_parameter("default_routing_policy", default_routing_policy)

    if hosts is not None:
        _details['hosts'] = cli_util.parse_json_parameter("hosts", hosts)

    if mtls is not None:
        _details['mtls'] = cli_util.parse_json_parameter("mtls", mtls)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_virtual_service(
        create_virtual_service_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_route_table_group.command(name=cli_util.override('service_mesh.create_virtual_service_route_table.command_name', 'create'), help=u"""Creates a new VirtualServiceRouteTable. \n[Command Reference](createVirtualServiceRouteTable)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""The OCID of the service mesh in which this access policy is created.""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation. Avoid entering confidential information.

Example: `My unique resource name`""")
@cli_util.option('--route-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The route rules for the virtual service.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--priority', type=click.INT, help=u"""The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'route-rules': {'module': 'service_mesh', 'class': 'list[VirtualServiceTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'route-rules': {'module': 'service_mesh', 'class': 'list[VirtualServiceTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'service_mesh', 'class': 'VirtualServiceRouteTable'})
@cli_util.wrap_exceptions
def create_virtual_service_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_id, name, route_rules, compartment_id, description, priority, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['virtualServiceId'] = virtual_service_id
    _details['name'] = name
    _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if priority is not None:
        _details['priority'] = priority

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.create_virtual_service_route_table(
        create_virtual_service_route_table_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@access_policy_group.command(name=cli_util.override('service_mesh.delete_access_policy.command_name', 'delete'), help=u"""Deletes an AccessPolicy resource by identifier. \n[Command Reference](deleteAccessPolicy)""")
@cli_util.option('--access-policy-id', required=True, help=u"""Unique AccessPolicy identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_access_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, access_policy_id, if_match):

    if isinstance(access_policy_id, six.string_types) and len(access_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --access-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.delete_access_policy(
        access_policy_id=access_policy_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_group.command(name=cli_util.override('service_mesh.delete_ingress_gateway.command_name', 'delete'), help=u"""Deletes an IngressGateway resource by identifier. \n[Command Reference](deleteIngressGateway)""")
@cli_util.option('--ingress-gateway-id', required=True, help=u"""Unique IngressGateway identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ingress_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ingress_gateway_id, if_match):

    if isinstance(ingress_gateway_id, six.string_types) and len(ingress_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.delete_ingress_gateway(
        ingress_gateway_id=ingress_gateway_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_route_table_group.command(name=cli_util.override('service_mesh.delete_ingress_gateway_route_table.command_name', 'delete'), help=u"""Deletes a IngressGatewayRouteTable resource by identifier. \n[Command Reference](deleteIngressGatewayRouteTable)""")
@cli_util.option('--ingress-gateway-route-table-id', required=True, help=u"""Unique IngressGatewayRouteTable identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ingress_gateway_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ingress_gateway_route_table_id, if_match):

    if isinstance(ingress_gateway_route_table_id, six.string_types) and len(ingress_gateway_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.delete_ingress_gateway_route_table(
        ingress_gateway_route_table_id=ingress_gateway_route_table_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mesh_group.command(name=cli_util.override('service_mesh.delete_mesh.command_name', 'delete'), help=u"""Deletes a Mesh resource by identifier. \n[Command Reference](deleteMesh)""")
@cli_util.option('--mesh-id', required=True, help=u"""Unique Mesh identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_mesh(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, mesh_id, if_match):

    if isinstance(mesh_id, six.string_types) and len(mesh_id.strip()) == 0:
        raise click.UsageError('Parameter --mesh-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.delete_mesh(
        mesh_id=mesh_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.delete_virtual_deployment.command_name', 'delete'), help=u"""Deletes a VirtualDeployment resource by identifier. \n[Command Reference](deleteVirtualDeployment)""")
@cli_util.option('--virtual-deployment-id', required=True, help=u"""Unique VirtualDeployment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_virtual_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_deployment_id, if_match):

    if isinstance(virtual_deployment_id, six.string_types) and len(virtual_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.delete_virtual_deployment(
        virtual_deployment_id=virtual_deployment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_group.command(name=cli_util.override('service_mesh.delete_virtual_service.command_name', 'delete'), help=u"""Deletes a VirtualService resource by identifier \n[Command Reference](deleteVirtualService)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""Unique VirtualService identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_virtual_service(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_id, if_match):

    if isinstance(virtual_service_id, six.string_types) and len(virtual_service_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.delete_virtual_service(
        virtual_service_id=virtual_service_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_route_table_group.command(name=cli_util.override('service_mesh.delete_virtual_service_route_table.command_name', 'delete'), help=u"""Deletes a VirtualServiceRouteTable resource by identifier. \n[Command Reference](deleteVirtualServiceRouteTable)""")
@cli_util.option('--virtual-service-route-table-id', required=True, help=u"""Unique VirtualServiceRouteTable identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_virtual_service_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_route_table_id, if_match):

    if isinstance(virtual_service_route_table_id, six.string_types) and len(virtual_service_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.delete_virtual_service_route_table(
        virtual_service_route_table_id=virtual_service_route_table_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@access_policy_group.command(name=cli_util.override('service_mesh.get_access_policy.command_name', 'get'), help=u"""Get an AccessPolicy by identifier. \n[Command Reference](getAccessPolicy)""")
@cli_util.option('--access-policy-id', required=True, help=u"""Unique AccessPolicy identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'AccessPolicy'})
@cli_util.wrap_exceptions
def get_access_policy(ctx, from_json, access_policy_id):

    if isinstance(access_policy_id, six.string_types) and len(access_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --access-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_access_policy(
        access_policy_id=access_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ingress_gateway_group.command(name=cli_util.override('service_mesh.get_ingress_gateway.command_name', 'get'), help=u"""Gets an IngressGateway by identifier. \n[Command Reference](getIngressGateway)""")
@cli_util.option('--ingress-gateway-id', required=True, help=u"""Unique IngressGateway identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'IngressGateway'})
@cli_util.wrap_exceptions
def get_ingress_gateway(ctx, from_json, ingress_gateway_id):

    if isinstance(ingress_gateway_id, six.string_types) and len(ingress_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_ingress_gateway(
        ingress_gateway_id=ingress_gateway_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ingress_gateway_route_table_group.command(name=cli_util.override('service_mesh.get_ingress_gateway_route_table.command_name', 'get'), help=u"""Gets a IngressGatewayRouteTable by identifier. \n[Command Reference](getIngressGatewayRouteTable)""")
@cli_util.option('--ingress-gateway-route-table-id', required=True, help=u"""Unique IngressGatewayRouteTable identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'IngressGatewayRouteTable'})
@cli_util.wrap_exceptions
def get_ingress_gateway_route_table(ctx, from_json, ingress_gateway_route_table_id):

    if isinstance(ingress_gateway_route_table_id, six.string_types) and len(ingress_gateway_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_ingress_gateway_route_table(
        ingress_gateway_route_table_id=ingress_gateway_route_table_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@mesh_group.command(name=cli_util.override('service_mesh.get_mesh.command_name', 'get'), help=u"""Gets a Mesh by identifier. \n[Command Reference](getMesh)""")
@cli_util.option('--mesh-id', required=True, help=u"""Unique Mesh identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'Mesh'})
@cli_util.wrap_exceptions
def get_mesh(ctx, from_json, mesh_id):

    if isinstance(mesh_id, six.string_types) and len(mesh_id.strip()) == 0:
        raise click.UsageError('Parameter --mesh-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_mesh(
        mesh_id=mesh_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@proxy_details_group.command(name=cli_util.override('service_mesh.get_proxy_details.command_name', 'get'), help=u"""Returns the attributes of the Proxy such as proxy image version. \n[Command Reference](getProxyDetails)""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'ProxyDetails'})
@cli_util.wrap_exceptions
def get_proxy_details(ctx, from_json, ):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_proxy_details(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.get_virtual_deployment.command_name', 'get'), help=u"""Gets a VirtualDeployment by identifier. \n[Command Reference](getVirtualDeployment)""")
@cli_util.option('--virtual-deployment-id', required=True, help=u"""Unique VirtualDeployment identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'VirtualDeployment'})
@cli_util.wrap_exceptions
def get_virtual_deployment(ctx, from_json, virtual_deployment_id):

    if isinstance(virtual_deployment_id, six.string_types) and len(virtual_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_virtual_deployment(
        virtual_deployment_id=virtual_deployment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_service_group.command(name=cli_util.override('service_mesh.get_virtual_service.command_name', 'get'), help=u"""Gets a VirtualService by identifier. \n[Command Reference](getVirtualService)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""Unique VirtualService identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'VirtualService'})
@cli_util.wrap_exceptions
def get_virtual_service(ctx, from_json, virtual_service_id):

    if isinstance(virtual_service_id, six.string_types) and len(virtual_service_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_virtual_service(
        virtual_service_id=virtual_service_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_service_route_table_group.command(name=cli_util.override('service_mesh.get_virtual_service_route_table.command_name', 'get'), help=u"""Gets a VirtualServiceRouteTable by identifier. \n[Command Reference](getVirtualServiceRouteTable)""")
@cli_util.option('--virtual-service-route-table-id', required=True, help=u"""Unique VirtualServiceRouteTable identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'VirtualServiceRouteTable'})
@cli_util.wrap_exceptions
def get_virtual_service_route_table(ctx, from_json, virtual_service_route_table_id):

    if isinstance(virtual_service_route_table_id, six.string_types) and len(virtual_service_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_virtual_service_route_table(
        virtual_service_route_table_id=virtual_service_route_table_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('service_mesh.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_policy_group.command(name=cli_util.override('service_mesh.list_access_policies.command_name', 'list'), help=u"""Returns a list of AccessPolicy objects. \n[Command Reference](listAccessPolicies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.""")
@cli_util.option('--mesh-id', help=u"""Unique Mesh identifier.""")
@cli_util.option('--id', help=u"""Unique AccessPolicy identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the life cycle state given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'AccessPolicyCollection'})
@cli_util.wrap_exceptions
def list_access_policies(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, mesh_id, id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if mesh_id is not None:
        kwargs['mesh_id'] = mesh_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_access_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_access_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_access_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ingress_gateway_route_table_group.command(name=cli_util.override('service_mesh.list_ingress_gateway_route_tables.command_name', 'list'), help=u"""Returns a list of IngressGatewayRouteTable objects. \n[Command Reference](listIngressGatewayRouteTables)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.""")
@cli_util.option('--ingress-gateway-id', help=u"""Unique IngressGateway identifier.""")
@cli_util.option('--id', help=u"""Unique IngressGatewayRouteTable identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the life cycle state given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'IngressGatewayRouteTableCollection'})
@cli_util.wrap_exceptions
def list_ingress_gateway_route_tables(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, ingress_gateway_id, id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if ingress_gateway_id is not None:
        kwargs['ingress_gateway_id'] = ingress_gateway_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ingress_gateway_route_tables,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ingress_gateway_route_tables,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_ingress_gateway_route_tables(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ingress_gateway_group.command(name=cli_util.override('service_mesh.list_ingress_gateways.command_name', 'list'), help=u"""Returns a list of IngressGateway objects. \n[Command Reference](listIngressGateways)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.""")
@cli_util.option('--mesh-id', help=u"""Unique Mesh identifier.""")
@cli_util.option('--id', help=u"""Unique IngressGateway identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the life cycle state given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'IngressGatewayCollection'})
@cli_util.wrap_exceptions
def list_ingress_gateways(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, mesh_id, id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if mesh_id is not None:
        kwargs['mesh_id'] = mesh_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ingress_gateways,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ingress_gateways,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_ingress_gateways(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@mesh_group.command(name=cli_util.override('service_mesh.list_meshes.command_name', 'list'), help=u"""Returns a list of Mesh objects. \n[Command Reference](listMeshes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire displayName given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the life cycle state given.""")
@cli_util.option('--id', help=u"""Unique Mesh identifier.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'MeshCollection'})
@cli_util.wrap_exceptions
def list_meshes(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by, lifecycle_state, id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_meshes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_meshes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_meshes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.list_virtual_deployments.command_name', 'list'), help=u"""Returns a list of VirtualDeployments. \n[Command Reference](listVirtualDeployments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.""")
@cli_util.option('--virtual-service-id', help=u"""Unique VirtualService identifier.""")
@cli_util.option('--id', help=u"""Unique VirtualDeployment identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the life cycle state given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'VirtualDeploymentCollection'})
@cli_util.wrap_exceptions
def list_virtual_deployments(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, virtual_service_id, id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if virtual_service_id is not None:
        kwargs['virtual_service_id'] = virtual_service_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_virtual_deployments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_virtual_deployments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_virtual_deployments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@virtual_service_route_table_group.command(name=cli_util.override('service_mesh.list_virtual_service_route_tables.command_name', 'list'), help=u"""Returns a list of VirtualServiceRouteTable objects. \n[Command Reference](listVirtualServiceRouteTables)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.""")
@cli_util.option('--virtual-service-id', help=u"""Unique VirtualService identifier.""")
@cli_util.option('--id', help=u"""Unique VirtualServiceRouteTable identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the life cycle state given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'VirtualServiceRouteTableCollection'})
@cli_util.wrap_exceptions
def list_virtual_service_route_tables(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, virtual_service_id, id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if virtual_service_id is not None:
        kwargs['virtual_service_id'] = virtual_service_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_virtual_service_route_tables,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_virtual_service_route_tables,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_virtual_service_route_tables(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@virtual_service_group.command(name=cli_util.override('service_mesh.list_virtual_services.command_name', 'list'), help=u"""Returns a list of VirtualService objects. \n[Command Reference](listVirtualServices)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.""")
@cli_util.option('--mesh-id', help=u"""Unique Mesh identifier.""")
@cli_util.option('--id', help=u"""Unique VirtualService identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the life cycle state given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'VirtualServiceCollection'})
@cli_util.wrap_exceptions
def list_virtual_services(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, mesh_id, id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if mesh_id is not None:
        kwargs['mesh_id'] = mesh_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_virtual_services,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_virtual_services,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_virtual_services(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('service_mesh.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('service_mesh.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('service_mesh.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--resource-id', help=u"""A filter to return work requests that match the given resourceId.""")
@cli_util.option('--operation-status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources that match the operation status given.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_mesh', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, resource_id, operation_status, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if operation_status is not None:
        kwargs['operation_status'] = operation_status
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@access_policy_group.command(name=cli_util.override('service_mesh.update_access_policy.command_name', 'update'), help=u"""Updates the AccessPolicy. \n[Command Reference](updateAccessPolicy)""")
@cli_util.option('--access-policy-id', required=True, help=u"""Unique AccessPolicy identifier.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of applicable rules.

This option is a JSON list with items of type AccessPolicyRuleDetails.  For documentation on AccessPolicyRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/AccessPolicyRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'rules': {'module': 'service_mesh', 'class': 'list[AccessPolicyRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'rules': {'module': 'service_mesh', 'class': 'list[AccessPolicyRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_access_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, access_policy_id, description, rules, freeform_tags, defined_tags, if_match):

    if isinstance(access_policy_id, six.string_types) and len(access_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --access-policy-id cannot be whitespace or empty string')
    if not force:
        if rules or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to rules and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if rules is not None:
        _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_access_policy(
        access_policy_id=access_policy_id,
        update_access_policy_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_group.command(name=cli_util.override('service_mesh.update_ingress_gateway.command_name', 'update'), help=u"""Updates the IngressGateway. \n[Command Reference](updateIngressGateway)""")
@cli_util.option('--ingress-gateway-id', required=True, help=u"""Unique IngressGateway identifier.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--hosts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of hostnames and their listener configuration that this gateway will bind to.

This option is a JSON list with items of type IngressGatewayHost.  For documentation on IngressGatewayHost please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/IngressGatewayHost.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--mtls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'hosts': {'module': 'service_mesh', 'class': 'list[IngressGatewayHost]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'mtls': {'module': 'service_mesh', 'class': 'IngressGatewayMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hosts': {'module': 'service_mesh', 'class': 'list[IngressGatewayHost]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'mtls': {'module': 'service_mesh', 'class': 'IngressGatewayMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_ingress_gateway(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ingress_gateway_id, description, hosts, access_logging, mtls, freeform_tags, defined_tags, if_match):

    if isinstance(ingress_gateway_id, six.string_types) and len(ingress_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-id cannot be whitespace or empty string')
    if not force:
        if hosts or access_logging or mtls or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to hosts and access-logging and mtls and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if hosts is not None:
        _details['hosts'] = cli_util.parse_json_parameter("hosts", hosts)

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if mtls is not None:
        _details['mtls'] = cli_util.parse_json_parameter("mtls", mtls)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_ingress_gateway(
        ingress_gateway_id=ingress_gateway_id,
        update_ingress_gateway_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ingress_gateway_route_table_group.command(name=cli_util.override('service_mesh.update_ingress_gateway_route_table.command_name', 'update'), help=u"""Updates the IngressGatewayRouteTable. \n[Command Reference](updateIngressGatewayRouteTable)""")
@cli_util.option('--ingress-gateway-route-table-id', required=True, help=u"""Unique IngressGatewayRouteTable identifier.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--priority', type=click.INT, help=u"""The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.""")
@cli_util.option('--route-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The route rules for the ingress gateway.

This option is a JSON list with items of type IngressGatewayTrafficRouteRuleDetails.  For documentation on IngressGatewayTrafficRouteRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/IngressGatewayTrafficRouteRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'route-rules': {'module': 'service_mesh', 'class': 'list[IngressGatewayTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'route-rules': {'module': 'service_mesh', 'class': 'list[IngressGatewayTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_ingress_gateway_route_table(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ingress_gateway_route_table_id, description, priority, route_rules, freeform_tags, defined_tags, if_match):

    if isinstance(ingress_gateway_route_table_id, six.string_types) and len(ingress_gateway_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --ingress-gateway-route-table-id cannot be whitespace or empty string')
    if not force:
        if route_rules or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to route-rules and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if priority is not None:
        _details['priority'] = priority

    if route_rules is not None:
        _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_ingress_gateway_route_table(
        ingress_gateway_route_table_id=ingress_gateway_route_table_id,
        update_ingress_gateway_route_table_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mesh_group.command(name=cli_util.override('service_mesh.update_mesh.command_name', 'update'), help=u"""Updates the Mesh. \n[Command Reference](updateMesh)""")
@cli_util.option('--mesh-id', required=True, help=u"""Unique Mesh identifier.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique and can be changed after creation. Avoid entering confidential information.

Example: `My new resource`""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--mtls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'mtls': {'module': 'service_mesh', 'class': 'MeshMutualTransportLayerSecurity'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'mtls': {'module': 'service_mesh', 'class': 'MeshMutualTransportLayerSecurity'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_mesh(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, mesh_id, display_name, description, mtls, freeform_tags, defined_tags, if_match):

    if isinstance(mesh_id, six.string_types) and len(mesh_id.strip()) == 0:
        raise click.UsageError('Parameter --mesh-id cannot be whitespace or empty string')
    if not force:
        if mtls or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to mtls and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if mtls is not None:
        _details['mtls'] = cli_util.parse_json_parameter("mtls", mtls)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_mesh(
        mesh_id=mesh_id,
        update_mesh_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.update_virtual_deployment.command_name', 'update'), help=u"""Updates the VirtualDeployment. \n[Command Reference](updateVirtualDeployment)""")
@cli_util.option('--virtual-deployment-id', required=True, help=u"""Unique VirtualDeployment identifier.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--service-discovery', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The listeners for the virtual deployment.

This option is a JSON list with items of type VirtualDeploymentListener.  For documentation on VirtualDeploymentListener please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/VirtualDeploymentListener.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-discovery': {'module': 'service_mesh', 'class': 'ServiceDiscoveryConfiguration'}, 'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-discovery': {'module': 'service_mesh', 'class': 'ServiceDiscoveryConfiguration'}, 'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_virtual_deployment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_deployment_id, description, service_discovery, listeners, access_logging, freeform_tags, defined_tags, if_match):

    if isinstance(virtual_deployment_id, six.string_types) and len(virtual_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-deployment-id cannot be whitespace or empty string')
    if not force:
        if service_discovery or listeners or access_logging or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-discovery and listeners and access-logging and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if service_discovery is not None:
        _details['serviceDiscovery'] = cli_util.parse_json_parameter("service_discovery", service_discovery)

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_virtual_deployment(
        virtual_deployment_id=virtual_deployment_id,
        update_virtual_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.update_virtual_deployment_dns_service_discovery_configuration.command_name', 'update-virtual-deployment-dns-service-discovery-configuration'), help=u"""Updates the VirtualDeployment. \n[Command Reference](updateVirtualDeployment)""")
@cli_util.option('--virtual-deployment-id', required=True, help=u"""Unique VirtualDeployment identifier.""")
@cli_util.option('--service-discovery-hostname', required=True, help=u"""The hostname of the virtual deployments.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The listeners for the virtual deployment.

This option is a JSON list with items of type VirtualDeploymentListener.  For documentation on VirtualDeploymentListener please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/VirtualDeploymentListener.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_virtual_deployment_dns_service_discovery_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_deployment_id, service_discovery_hostname, description, listeners, access_logging, freeform_tags, defined_tags, if_match):

    if isinstance(virtual_deployment_id, six.string_types) and len(virtual_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-deployment-id cannot be whitespace or empty string')
    if not force:
        if listeners or access_logging or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to listeners and access-logging and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceDiscovery'] = {}
    _details['serviceDiscovery']['hostname'] = service_discovery_hostname

    if description is not None:
        _details['description'] = description

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['serviceDiscovery']['type'] = 'DNS'

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_virtual_deployment(
        virtual_deployment_id=virtual_deployment_id,
        update_virtual_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_deployment_group.command(name=cli_util.override('service_mesh.update_virtual_deployment_disabled_service_discovery_configuration.command_name', 'update-virtual-deployment-disabled-service-discovery-configuration'), help=u"""Updates the VirtualDeployment. \n[Command Reference](updateVirtualDeployment)""")
@cli_util.option('--virtual-deployment-id', required=True, help=u"""Unique VirtualDeployment identifier.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The listeners for the virtual deployment.

This option is a JSON list with items of type VirtualDeploymentListener.  For documentation on VirtualDeploymentListener please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/VirtualDeploymentListener.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-logging', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'listeners': {'module': 'service_mesh', 'class': 'list[VirtualDeploymentListener]'}, 'access-logging': {'module': 'service_mesh', 'class': 'AccessLoggingConfiguration'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_virtual_deployment_disabled_service_discovery_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_deployment_id, description, listeners, access_logging, freeform_tags, defined_tags, if_match):

    if isinstance(virtual_deployment_id, six.string_types) and len(virtual_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-deployment-id cannot be whitespace or empty string')
    if not force:
        if listeners or access_logging or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to listeners and access-logging and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceDiscovery'] = {}

    if description is not None:
        _details['description'] = description

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if access_logging is not None:
        _details['accessLogging'] = cli_util.parse_json_parameter("access_logging", access_logging)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['serviceDiscovery']['type'] = 'DISABLED'

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_virtual_deployment(
        virtual_deployment_id=virtual_deployment_id,
        update_virtual_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_group.command(name=cli_util.override('service_mesh.update_virtual_service.command_name', 'update'), help=u"""Updates the VirtualService. \n[Command Reference](updateVirtualService)""")
@cli_util.option('--virtual-service-id', required=True, help=u"""Unique VirtualService identifier.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--default-routing-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hosts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The DNS hostnames of the virtual service that is used by its callers. Wildcard hostnames are supported in the prefix form. Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\". Can be omitted if the virtual service will only have TCP virtual deployments.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--mtls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'default-routing-policy': {'module': 'service_mesh', 'class': 'DefaultVirtualServiceRoutingPolicy'}, 'hosts': {'module': 'service_mesh', 'class': 'list[string]'}, 'mtls': {'module': 'service_mesh', 'class': 'VirtualServiceMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'default-routing-policy': {'module': 'service_mesh', 'class': 'DefaultVirtualServiceRoutingPolicy'}, 'hosts': {'module': 'service_mesh', 'class': 'list[string]'}, 'mtls': {'module': 'service_mesh', 'class': 'VirtualServiceMutualTransportLayerSecurityDetails'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_virtual_service(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_id, description, default_routing_policy, hosts, mtls, freeform_tags, defined_tags, if_match):

    if isinstance(virtual_service_id, six.string_types) and len(virtual_service_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-id cannot be whitespace or empty string')
    if not force:
        if default_routing_policy or hosts or mtls or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to default-routing-policy and hosts and mtls and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if default_routing_policy is not None:
        _details['defaultRoutingPolicy'] = cli_util.parse_json_parameter("default_routing_policy", default_routing_policy)

    if hosts is not None:
        _details['hosts'] = cli_util.parse_json_parameter("hosts", hosts)

    if mtls is not None:
        _details['mtls'] = cli_util.parse_json_parameter("mtls", mtls)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_virtual_service(
        virtual_service_id=virtual_service_id,
        update_virtual_service_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_service_route_table_group.command(name=cli_util.override('service_mesh.update_virtual_service_route_table.command_name', 'update'), help=u"""Updates the VirtualServiceRouteTable. \n[Command Reference](updateVirtualServiceRouteTable)""")
@cli_util.option('--virtual-service-route-table-id', required=True, help=u"""Unique VirtualServiceRouteTable identifier.""")
@cli_util.option('--description', help=u"""Description of the resource. It can be changed after creation. Avoid entering confidential information.

Example: `This is my new resource`""")
@cli_util.option('--priority', type=click.INT, help=u"""The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.""")
@cli_util.option('--route-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The route rules for the virtual service.

This option is a JSON list with items of type VirtualServiceTrafficRouteRuleDetails.  For documentation on VirtualServiceTrafficRouteRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/servicemesh/20220615/datatypes/VirtualServiceTrafficRouteRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "WAITING", "NEEDS_ATTENTION", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'route-rules': {'module': 'service_mesh', 'class': 'list[VirtualServiceTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'route-rules': {'module': 'service_mesh', 'class': 'list[VirtualServiceTrafficRouteRuleDetails]'}, 'freeform-tags': {'module': 'service_mesh', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'service_mesh', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_virtual_service_route_table(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_service_route_table_id, description, priority, route_rules, freeform_tags, defined_tags, if_match):

    if isinstance(virtual_service_route_table_id, six.string_types) and len(virtual_service_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-service-route-table-id cannot be whitespace or empty string')
    if not force:
        if route_rules or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to route-rules and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if priority is not None:
        _details['priority'] = priority

    if route_rules is not None:
        _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('service_mesh', 'service_mesh', ctx)
    result = client.update_virtual_service_route_table(
        virtual_service_route_table_id=virtual_service_route_table_id,
        update_virtual_service_route_table_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
