import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class UserSolution {

    private HashMap<String, ArrayList<HashMap<Integer, Integer>>> userHashMap;
    private HashMap<Integer, Object> userIdOfInfo;

	public void init() {

        this.userHashMap = new HashMap<>();
        this.userIdOfInfo = new HashMap<>();
		return;
	}

	public int add(int mId, int mGrade, char mGender[], int mScore) {
        HashMap<String, Object> userInfo = new HashMap<>();

        String gender = new String(mGender).replace("\0", "");

        userInfo.put("userId", mId);
        userInfo.put("grade", mGrade);
        userInfo.put("gender", gender);
        userInfo.put("score", mScore);

        ArrayList<HashMap<Integer, Integer>> userList = userHashMap.get(gender);
        if (userList == null){
            userList = new ArrayList<>();

            userList.add(new HashMap<>());
            userList.add(new HashMap<>());
            userList.add(new HashMap<>());

            userHashMap.put(gender, userList);
        }
        userList = userHashMap.get(gender);
        userList.get(mGrade - 1).put(mId, mScore);
        userIdOfInfo.put(mId, userInfo);
        
        int maxScoreUserId = findMaxScoreByGradeAndGender(mGrade, gender);
		return maxScoreUserId;
	}

	public int remove(int mId) {
        HashMap<String, Object> removeUserInfo = (HashMap<String, Object>) userIdOfInfo.get(mId);

        if (removeUserInfo == null){
            return 0;
        }

        int mGrade = Integer.parseInt(removeUserInfo.get("grade").toString());
        String mGender = removeUserInfo.get("gender").toString();
        HashMap<Integer, Integer> newUserInfo = userHashMap.get(mGender).get(mGrade-1);

        userIdOfInfo.remove(mId);
        newUserInfo.remove(mId);

        userHashMap.get(mGender).set(mGrade-1, newUserInfo);

        int nextUserId = 1000000001;
        int minScore = 300001;

        
        Set keys = newUserInfo.keySet();
        Iterator iterator = keys.iterator();
        boolean flag = false;
        while(iterator.hasNext()){
            int key = (int) iterator.next();

            int score = newUserInfo.get(key);

            if(minScore > score){
                nextUserId = key;
                minScore = score;
                flag = true;
            } else if(minScore == score && nextUserId > key){
                nextUserId = key;
                minScore = score;
                flag = true;
            }
        }
        
        if (flag == false){
            return 0;
        }
		return nextUserId;
	}

	public int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][], int mScore) {
        HashMap<Integer, Integer> queryResultMap = new HashMap<>();

        for (int j= 0; j<mGenderCnt; j++){
            for(int i = 0; i<mGradeCnt; i++){
                try{
                    queryResultMap.putAll(userHashMap.get(new String(mGender[j])).get(mGrade[i]-1));
                } catch (NullPointerException e){
                    continue;
                }
            }
        }

        int nextUserId = 1000000001;
        int minScore = 300001;

        Set keys = queryResultMap.keySet();
        Iterator iterator = keys.iterator();
        boolean flag = false;

        while(iterator.hasNext()){

            int key = (int) iterator.next();
            int score = queryResultMap.get(key);

            if(score >= mScore){
                if(nextUserId > key && minScore == score){
                    nextUserId = key;
                    minScore = score;
                    flag = true;
                }
                else if(minScore > score){
                    nextUserId = key;
                    minScore = score;
                    flag = true;
                }
            }
            
        }

        if(flag == false){
            return 0;
        }

        return nextUserId;
	}

    public int findMaxScoreByGradeAndGender(int mGrade, String mGender){
        int findId = 0;
        int maxScore = 0;

        HashMap<Integer, Integer> userList = userHashMap.get(mGender).get(mGrade-1);

        Set keys = userList.keySet();
        Iterator iterator = keys.iterator();
        
        while(iterator.hasNext()){

            int key = (int) iterator.next();
            int score = userList.get(key);

            if(maxScore < score){
                findId = key;
                maxScore = score;
            }
            else if(maxScore == score && findId < key){
                findId = key;
                maxScore = score;
            }
            
        }

        return findId;
    }

    public boolean checkCondition(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][], int mScore, int grade, String gender, int score){

        boolean flag1 = false;
        boolean flag2 = false;
        boolean flag3 = false;

        for(int i=0; i<mGenderCnt; i++){
            if (grade == mGrade[i]){
                flag1 = true;
            }
        }

        for(int i=0; i<mGenderCnt; i++){
            if(gender.equals(new String(mGender[i]))){
                flag2 = true;
            }
        }

        if (score >= mScore){
            flag3 = true;
        }
        if(flag1 == true && flag2 == true && flag3 == true ){
            return true;
        }
        return false;
    }
}