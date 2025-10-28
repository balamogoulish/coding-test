class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "fail";
        for(String[] ac: db){
            if(ac[0].equals(id_pw[0])){
                if(ac[1].equals(id_pw[1])) return "login";
                return "wrong pw";
            }
        }
        return answer;
    }
}