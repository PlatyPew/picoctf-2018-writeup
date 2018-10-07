/*
int validate_key(int arg0) {
    var_4 = arg0;
    esp = (esp - 0x10) + 0x10;
    var_C = strlen(var_4);
    var_14 = 0x0;
    for (var_10 = 0x0; var_C - 0x1 > var_10; var_10 = var_10 + 0x1) {
            esp = (esp - 0x10) + 0x10;
            var_14 = var_14 + (var_10 + 0x1) * (sign_extend_32(ord(sign_extend_32(*(int8_t *)(var_4 + var_10) & 0xff))) + 0x1);
    }
    eax = *(int8_t *)(var_4 + (var_C - 0x1)) & 0xff;
    eax = ord(sign_extend_32(eax));
    eax = var_14 - ((HIDWORD(var_14 * 0x38e38e39) >> 0x3 << 0x3) + (HIDWORD(var_14 * 0x38e38e39) >> 0x3) << 0x2) == sign_extend_32(eax) ? 0x1 : 0x0;
    return eax;
}
*/

int validate_key(int keyArgs) {
    key = keyArgs;
    esp = (esp - 0x10) + 0x10;
    key_length = strlen(key);
    var_14 = 0;
    for (int i = 0; key_length - 1 > i; i++) {
            esp = (esp - 0x10) + 0x10;
            var_14 += (i + 1) * (sign_extend_32(ord(sign_extend_32(*(int8_t *)(var_4 + i) & 0xff))) + 0x1);
    }
    eax = *(int8_t *)(key + (key_length - 0x1)) & 0xff;
    eax = ord(sign_extend_32(eax));
    eax = var_14 - ((HIDWORD(var_14 * 0x38e38e39) >> 0x3 << 0x3) + (HIDWORD(var_14 * 0x38e38e39) >> 0x3) << 0x2) == sign_extend_32(eax) ? 0x1 : 0x0;
    return eax;
}
