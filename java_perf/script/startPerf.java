// 定义节点类
class Node {
    public int data;
    public Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// 定义链表类
class LinkedList {
    private Node head;
    private Node tail;
    private int len;
    // 在链表的末尾添加新节点
    public void append_effective(int data) {
        if (head == null || tail == null) {
	    head = new Node(data);
            tail = head;
	    len++;
	    return;
        }
	Node newTail = new Node(data);
	tail.next = newTail;
	tail = newTail;
	len++;
    }

    public void append_ineffective(int data){
    	if (head == null) {
            head = new Node(data);
            len++;
            return;
	}
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = new Node(data);
	len++;
    }

    public int getlen() {
    	return len;
    }

    public Node gethead(){
    	return head;
    }
}



// 主类
public class startPerf {
   static void addToList_effective(LinkedList list){
	for (int i = 0; i < 1e5; i++)
	    list.append_effective(i);
   }
   static void addToList_ineffective(LinkedList list){
   	for (int i = 0; i < 1e5; i++)
	    list.append_ineffective(i);
   }
   public static void main(String[] args) {
        LinkedList list01 = new LinkedList();	
   	LinkedList list02 = new LinkedList(); 
   	addToList_effective(list01);
	addToList_ineffective(list02);
   }
}
