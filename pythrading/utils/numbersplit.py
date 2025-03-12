def make_comma(value: float) -> str:
    value = round(value)  # 반올림
    strValue: str = str(value)
    newValue: str = ""
    if len(strValue) > 3:
        for i in range(len(strValue)):
            if i % 3 == 0 and i != 0:
                newValue += "," + strValue[i]
            else:
                newValue += strValue[i]
    return newValue