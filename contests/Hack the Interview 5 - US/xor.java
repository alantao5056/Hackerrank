public class xor {
  public static void main(String[] args) {
    System.out.println(maxXorValue("01010", 1));
  }

  public static String maxXorValue(String x, int k) {
    int count = 0;
    String result = "";
    for (int i = 0; i < x.length(); i ++) {
      if (count < k) {
        if (x.charAt(i) == '0') {
          result += "1";
          count += 1;
        } else {
          result += "0";
        }
      } else {
        break;
      }
    }
    for (int i = result.length(); i < x.length(); i++) {
      result += '0';
    }
    return result;
  }
}
