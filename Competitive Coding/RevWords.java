class RevWords{
    static char[] reverseWords(char[] s)
    {
        int start = 0;
        for (int end = 0; end < s.length; end++)
        {
            if (s[end] == ' ')
            {
                reverse(s, start, end);
                start = end + 1;
            }
        }

        // reverse last word
        reverse(s, start, s.length - 1);

        // reverse entire String
        reverse(s, 0, s.length - 1);
        return s;
    }
    static void reverse(char str[],
                        int start,
                        int end)
    {
        char temp;

        while (start <= end)
        {
            temp = str[start];
            str[start] = str[end];
            str[end] = temp;
            start++;
            end--;
        }
    }

    public static void main(String[] args)
    {
        String s = "The String to be reversed "; //This is the string whose words will be reversed
        char[] p = reverseWords(s.toCharArray());
        System.out.print(p);
    }
}