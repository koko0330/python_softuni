# --- Constants --- #

LIGHT_LIMIT  = 100
LIMIT_CNT_TRIGGER = 2

# --- Global vars --- #

_limitCnt = 0

# --- light_limitCheck
# params:
#   light_limit - The limit that we use to check against
# the current light volume
#   light_volute - The measured light volume from the sensor
# returns:
#   True - if the light_volume is two consequtive times under the limit
#   False - in any other case
def _lights_limitCheck(light_limit, light_volume):
    global _limitCnt

    if light_volume < light_limit:
        _limitCnt += 1
        print("Number of times under the limit: %d" % _limitCnt)
    elif light_volume >= light_limit:
        _limitCnt -= 1

    if _limitCnt == LIMIT_CNT_TRIGGER:
        _limitCnt = 0
        return True
    else:
        return False

# --- main
def main():
    print("Light limit:%d " % LIGHT_LIMIT)


    ret = _lights_limitCheck(LIGHT_LIMIT, 12)
    print(ret)

    ret = _lights_limitCheck(LIGHT_LIMIT, 12)
    print(ret)


    ret = _lights_limitCheck(LIGHT_LIMIT, 543)
    print(ret)

    ret = _lights_limitCheck(LIGHT_LIMIT, 123)
    print(ret)

if __name__ == "__main__":
    main()


