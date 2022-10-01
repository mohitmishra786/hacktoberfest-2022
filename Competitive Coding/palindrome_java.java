publi class Palindrome {
    public static void main(String[] args) {
        String value = "level"; // Replace word for check Palindrome
        int i = 0;
        if (i < value.length() / 2) {
            if (value.charAt(i) != value.charAt(value.length() - 1)) {
                System.out.print("Not Palindrome");
            } else {
                System.out.print("Palindrome");
            }
        }
    }
}
