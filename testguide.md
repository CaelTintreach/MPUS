# Test Guide

To carry out tests for this software, please see the provided tests files and use pytest for existing tests and coverage purposes.



For those wishing to add integration tests for the purposes of trialling their own fixes for updating user stories, copy the format used in the update project integration test with the provided variables.



## Test Results

Testing has been carried out on this version of the software to cover all major areas of functionality, however it should be noted that integration tests have not been implemented for Update User Stories as this functionality is currently broken and the time was better spent attempting to instead resolve the issue. In the future once the feature breakage has been resolved then tests will be added to provide integration coverage for this feature.



Unit Testing has achieved up to a coverage of 91% on the software and consistently scored 89% coverage otherwise. These missing areas have been noticed (the functions in routes.py which control the elif statement for not ) and will be covered by testing in the next version of the software release.