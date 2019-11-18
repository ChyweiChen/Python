# PROGRAM MatchingPatterns:

import re

search_string = "hello world"
pattern       = "hello world"

match = re.match(pattern, search_string)

if match:
    # THEN
    print("regex matches")
else:
    print("No match")
# ENDIF;

# END.
