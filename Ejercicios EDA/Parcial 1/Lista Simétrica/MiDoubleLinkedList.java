package packObtenerListaSimetrica;

import packPruebaDebugger.EstructuraArray;
import packPruebaDebugger.EstructuraEnlazada;
import packPruebaDebugger.Persona;

public class MiDoubleLinkedList {// Lista circular doblemente enlazada
	DoubleNode<Integer> first;

	public void obtenerListaSimetrica(SimpleLinkedList l) {
		// Pre: la lista "l" contiene valores positivos distintos de cero (x, y,
		// ... z)
		// Post: el resultado es una lista del tipo (-x, -y, ... -z, z ... y, x)
		// donde cada elemento x de la lista original aparece dos veces (-x, x)
		// de manera simétrica

		Node<Integer> act = l.first;
		


































	}
	
	public Integer removeFirst() {
		if (this.first == null) return null;
		else {
			Integer elem = this.first.data;
			if (this.first.next == this.first) this.first = null; // eliminar en lista de 1 solo elemento
			else {
				this.first.next.prev = this.first.prev;
				this.first.prev.next = this.first.next;
				this.first = this.first.next;
			}
			return elem;
		}
	}
	
	public void print() {
		DoubleNode<Integer> act = this.first;
		System.out.print("[ ");
		if (act == null) {}
		else {
			System.out.print(act.data); // escribir el primero
			act = act.next;
			while (act != this.first) {
				System.out.print(", " + act.data);
				act = act.next;
			}
		}
		System.out.println(" ]");		
	}
	
	public static void main(String[] args) {

		// Primera prueba: lista vacía
		System.out.println("El resultado de bería ser la lista vacía: ");
		MiDoubleLinkedList lista = new MiDoubleLinkedList();
		lista.obtenerListaSimetrica(new SimpleLinkedList());
		lista.print();
		if (lista.first != null) System.out.println("Error en prueba 1");
		else System.out.println("Prueba 1 OK");

		// Segunda prueba: lista no vacía
		SimpleLinkedList l = new SimpleLinkedList();
		l.crearListaEjemplo();
		System.out.println("El resultado debería ser la lista [ -1, -4, -3, -8, 8, 3, 4, 1 ]: ");
		lista = new MiDoubleLinkedList();
		lista.obtenerListaSimetrica(l);
		lista.print();
		Integer[] a = {-1, -4, -3, -8, 8, 3, 4, 1}; // Este debería ser el resultado
		boolean error = false;
		for (Integer x: a) {
			Integer elem = lista.removeFirst();
			if (x != elem) {
				System.out.println("Error en prueba 2: " + x + " " + elem );
				error = true;
			}
		}
		if (lista.first != null) System.out.println("Error en prueba 2: ");
		else if (!error) System.out.println("Prueba 2 OK");

		

	}
}
