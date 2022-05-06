package packObtenerListaSimetrica;

public class SimpleLinkedList {// Lista circular doblemente enlazada

	Node<Integer> first;
	
	public void crearListaEjemplo() {
		// Post: crea una lista de ejemplo con los valores (8, 3, 4, 1)
		
		Node<Integer> n1 = new Node<Integer>();
		n1.data = 8;
		Node<Integer> n2 = new Node<Integer>();
		n2.data = 3;
		Node<Integer> n3 = new Node<Integer>();
		n3.data = 4;
		Node<Integer> n4 = new Node<Integer>();
		n4.data = 1;
		n1.next = n2;
		n2.next = n3;
		n3.next = n4;
		first = n1;
	}
	
}
