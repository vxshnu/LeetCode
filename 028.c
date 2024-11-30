int strStr(char* haystack, char* needle) {
    char *occ = strstr(haystack,needle);
    if(occ != NULL)
    return occ - haystack;
    else
    return -1;
}