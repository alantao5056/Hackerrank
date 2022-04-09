class keyboard {

  /*
   * Complete the 'receivedText' function below.
   *
   * The function is expected to return a STRING.
   * The function accepts STRING S as parameter.
  */

  public static void main(String[] args) {
    System.out.println(receivedText("HE*<LL>O"));
  }

  public static String receivedText(String S) {
    // WRITE DOWN YOUR CODE HERE
    String result = "";
    int curser = -1;
    Boolean numLock = false;

    for (int i = 0; i < S.length(); i++) {
      char c = S.charAt(i);
      if (c == '*') {
        // backspace
        if (curser > 0) {
          result = result.substring(0, curser) + result.substring(curser + 1, result.length());
          curser -= 1;
        }
      } else if (c == '<') {
        // home button
        curser = -1;
      } else if (c == '>') {
        // end button
        if (curser != -1) {
          curser = result.length() - 1;
        }
      } else if (c == '#') {
        // numlock
        if (numLock) {
          numLock = false;
        } else {
          numLock = true;
        }
      } else {
        // letter or number
        if (isNumeric(Character.toString(c))) {
          if (numLock) {
            continue;
          }
        }
        if (result.length() == 0) {
          result = Character.toString(c);
        } else {
          result = result.substring(0, curser + 1) + Character.toString(c) + result.substring(curser + 1, result.length());
        }
        curser += 1;
      }
    }

    return result;
  }

  public static boolean isNumeric(String str) { 
    try {  
      Double.parseDouble(str);  
      return true;
    } catch(NumberFormatException e){  
      return false;  
    }  
  }

}