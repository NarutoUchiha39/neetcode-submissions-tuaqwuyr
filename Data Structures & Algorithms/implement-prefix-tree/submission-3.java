

class Node{
    HashMap<String,Node> children;
    boolean is_word_end;
    public Node(){
        this.children = new HashMap<>();
        this.is_word_end = false;
    }
}

class PrefixTree {

    Node root;
    public PrefixTree() {
         this.root = new Node();
    }

    public void insert(String word) {
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
        Node node = this.root;

        for(int i=0;i<word.length();i++){
            char curChar = word.charAt(i);
            String curString = new String(new char[]{curChar});
            // System.out.println(" i "+i+" "+node.children);
            if(!node.children.containsKey(curString)){
                return false;
            }
            node = node.children.get(curString);
        }

        return true && node.is_word_end;

    }

    public boolean startsWith(String word) {

        Node node = this.root;

        for(int i=0;i<word.length();i++){
            char curChar = word.charAt(i);
            String curString = new String(new char[]{curChar});
            if(!node.children.containsKey(curString)){
                return false;
            }
            node = node.children.get(curString);
        }

        return true;
        
    }
}
