// import java.util.HashMap;

class Node{
        HashMap<String,Node> children;
        boolean is_word_end;
        public Node(){
            this.children = new HashMap<>();
            this.is_word_end = false;
        }
}

public class WordDictionary {
    
    Node root;
    public WordDictionary() {
        this.root = new Node();
    }

    public boolean helper(Node node,String word,int index){

        if (index == word.length()) {
            if(node.is_word_end){
                return true;
            }
            return false;
        }

        char curChar = word.charAt(index);
        String curString = new String(new char[]{curChar});

        if (curString .equals(".")) {
            for(String a: node.children.keySet()){
                boolean res = helper(node.children.get(a), word, index+1);
                if (res) {
                    return true;
                }
            }
        }
        else if (node.children.containsKey(curString)) {
            return helper(node.children.get(curString), word, index+1);
        }

        return false;
    }

    public void addWord(String word) {
        Node copy = this.root;
            for(int i=0;i<word.length();i++){
                char curChar = word.charAt(i);
                String curString = new String(new char[]{curChar});
                if(!copy.children.containsKey(curString)){
                    copy.children.put(curString, new Node());
                }
                copy = copy.children.get(curString);
        }
        copy.is_word_end = true;
    }

    public boolean search(String word) {
        return helper(root, word, 0);
    }
}