#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CourseBuilder.settings")
    from django.core.management import execute_from_command_line
    import CourseBuilder.startup as startup
    startup.run()
    execute_from_command_line(sys.argv)
