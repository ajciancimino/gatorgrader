"""Orchestrate the checks performed on writing and source code"""

import sys

# pylint: disable=unused-import
from gator import arguments
from gator import display
from gator import invoke
from gator import leave
from gator import report
from gator import run

DISPLAY = sys.modules["gator.display"]
INVOKE = sys.modules["gator.invoke"]
ORCHESTRATE = sys.modules[__name__]
RUN = sys.modules["gator.run"]

VOID = []

INCORRECT_ARGUMENTS = 2

REPOSITORY = "."


def check_arguments(system_arguments):
    """Check the arguments return the desired actions to perform"""
    # parse and verify the arguments
    actions = []
    gg_arguments = arguments.parse(system_arguments)
    # Action: display the welcome message
    if gg_arguments.nowelcome is not True:
        actions.append([DISPLAY, "welcome_message", VOID])
    did_verify_arguments = arguments.verify(gg_arguments)
    # arguments are incorrect
    if did_verify_arguments is False:
        # Action: display incorrect arguments message
        actions.append([DISPLAY, "incorrect_message", VOID])
        # Action: exit the program
        actions.append([RUN, "run_exit", [INCORRECT_ARGUMENTS]])
    return gg_arguments, actions


def check_commits(system_arguments):
    """Check the commits to the git repository and return desired actions"""
    actions = []
    if system_arguments.commits is not None:
        actions.append(
            [INVOKE, "invoke_commits_check", [REPOSITORY, system_arguments.commits]]
        )
    return actions


def check_exists(system_arguments):
    """Check the existence of a file in directory and return desired actions"""
    actions = []
    if system_arguments.exists is True:
        actions.append(
            [
                INVOKE,
                "invoke_file_in_directory_check",
                [system_arguments.file, system_arguments.directory],
            ]
        )
    return actions


def perform(actions):
    """Perform the specified actions"""
    results = []
    # iteratively run all of the actions in the list
    for module, function, parameters in actions:
        function_to_invoke = getattr(module, function)
        # no parameters were specified, do not pass
        if parameters == []:
            function_result = function_to_invoke()
        # parameters were specified, do pass
        else:
            function_result = function_to_invoke(*parameters)
        results.append(function_result)
    return results


def check(system_arguments):
    """Orchestrate a full check of the specified deliverables"""
    # Section: Initialize
    # Only step: check the arguments
    gg_arguments, arguments_actions = check_arguments(system_arguments)
    step_results = []
    check_results = []
    step_results = perform(arguments_actions)
    check_results = check_results + step_results
    # Section: Perform one of these steps
    # Step: check the commit status
    actions = check_commits(gg_arguments)
    step_results = perform(actions)
    check_results = check_results + step_results
    # Step: check the existence of a file
    actions = check_exists(gg_arguments)
    step_results = perform(actions)
    check_results = check_results + step_results
    # Section: Output the report
    # Only step: get the report's details, produce the output, and display it
    output_list = report.output_list(report.get_details(), report.TEXT)
    produced_output = report.output(output_list)
    display.message(produced_output)
    # Section: Return control back to __main__ in gatorgrader
    # Only step: determine the correct exit code for the checks
    correct_exit_code = leave.get_code(check_results)
    return correct_exit_code
