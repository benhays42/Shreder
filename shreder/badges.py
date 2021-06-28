#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

class Badges:
    logfilehandler = None

    def print_empty(self, message="", end='\n'):
        if self.logfilehandler:
            self.logfilehandler.write(message + end)
        print(f"\033[1K\r{message}", end=end)

    @staticmethod
    def print_process(message, end='\n'):
        print(f"\033[1K\r\033[1;34m[*]\033[0m {message}", end=end)

    def print_success(self, message, end='\n'):
        if self.logfilehandler:
            self.logfilehandler.write("[SUCCESS] " + message + end)
        print(f"\033[1K\r\033[1;32m[+]\033[0m {message}", end=end)

    def print_error(self, message, end='\n'):
        if self.logfilehandler:
            self.logfilehandler.write("[ERROR] " + message + end)
        print(f"\033[1K\r\033[1;31m[-]\033[0m {message}", end=end)

    def print_warning(self, message, end='\n'):
        if self.logfilehandler:
            self.logfilehandler.write("[WARN] " + message + end)
        print(f"\033[1K\r\033[1;33m[!]\033[0m {message}", end=end)

    def print_information(self, message, end='\n'):
        if self.logfilehandler:
            self.logfilehandler.write("[INFO] " + message + end)
        print(f"\033[1K\r\033[1;77m[i]\033[0m {message}", end=end)
