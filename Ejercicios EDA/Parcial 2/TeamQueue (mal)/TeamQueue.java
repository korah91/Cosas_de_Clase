
import java.awt.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class TeamQueue {


	Queue<Queue<Integer>> q;
	HashMap<Integer, Integer> teams; 
	// clave: persona, valor: número del grupo al que pertenece esa persona

	public TeamQueue() {
		q = (Queue<Queue<Integer>>) new LinkedList();
		teams = new HashMap<Integer, Integer>();
		// Grupo A: 1, 5, 7
		// Grupo B: 2, 4, 8, 10
		// Grupo C: 3, 6, 11
		teams.put(1, 1);
		teams.put(5, 1);
		teams.put(7, 1);
		teams.put(2, 2);
		teams.put(4, 2);
		teams.put(8, 2);
		teams.put(10, 2);
		teams.put(3, 3);
		teams.put(6, 3);
		teams.put(11, 3);

	}
	

	
	public void enqueue(int x){
		Queue<Queue<Integer>> aux = (Queue<Queue<Integer>>) new LinkedList(); // para guardar los elementos de la cola
		boolean added = false;
		
		while (!q.isEmpty()){
			// COMPLETAR CÓDIGO
			boolean enc = false;

			for (Queue<Integer> cola : q)
			{
				if(mismoGrupo(x, q.first()))
				{

				}

			}
		}

		if (!added)
		{ // la persona que entra no ha encontrado a nadie de su grupo. Se pone al final
						// COMPLETAR CÓDIGO
		}




		q = aux;
		
	}
	

	
	public void dequeue(){
		// Pre: cola no vacía
		if (!q.isEmpty()){
			int borrado = q.peek().remove();
			if (q.peek().isEmpty()) q.remove(); // si se ha sacado el último elemento de la primera cola, se quita
			System.out.println("Ha salido el " + borrado);
		}
	}	
	
	
	public void print(){
		// imprime el contenido de la cola, sin modificarla
		for (Queue<Integer> c: q){
			System.out.print("[");
			for (Integer x: c) System.out.print(x + " ");
			System.out.print("] ");
		}
		System.out.println();
	}

	public boolean mismoGrupo(int p1, int p2)
	{
		boolean enc = false
		for (Integer i : teams.keySet())
		{
			if()
		}
		return enc;
	}

	
	private void test() {
		TeamQueue tq = new TeamQueue();
		tq.enqueue(2);
		tq.print();
		tq.enqueue(6);
		tq.print();
		tq.enqueue(8);
		tq.print();
		tq.enqueue(5);
		tq.print();
		tq.enqueue(4);
		tq.print();
		tq.enqueue(1);
		tq.print();
		tq.enqueue(3);
		tq.print();
		tq.dequeue();
		tq.print();
		tq.dequeue();
		tq.print();
		tq.dequeue();
		tq.print();
		tq.enqueue(11);
		tq.print();
	}

	public static void main(String[] args) {
	
		new TeamQueue().test();
	}
}
