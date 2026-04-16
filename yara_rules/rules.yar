rule suspicious_word
{
    strings:
        $phish = "password"
    condition:
        $phish
}