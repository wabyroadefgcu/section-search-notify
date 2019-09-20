#!/usr/bin/env python3

import emailer.email_results as email_results

result = email_results.email_section_list("Test Subject", "Test Message")
print("\n")
print(result)
