import java.util.ArrayList;

public class Camino {
    Node first;
    public CircularLinkedList<String> obtCoordenadas(ArrayList<String> acciones) {
        // pre: la lista acciones tiene al menos un elemento, e indica los
        // movimientos a realizar por el robot
        // El recorrido no produce error (nunca se intenta avanzar por un
        // enlace con valor null)

        // post: devuelve una nueva lista, que contendrá
        // las coordenadas de los puntos recorridos
        // La lista original no se ha modificado
        CircularLinkedList<String> res = new CircularLinkedList<>();
        res.last = new NodeCircularLinkedList<String>();
        res.last.data = first.coord;

        Node aux = first;
        int i_acciones = 0;

        while(i_acciones < acciones.size())
        {
            if(acciones.get(i_acciones).equals("izquierda"))
            {
                aux = aux.left;
            }
            else if(acciones.get(i_acciones).equals("derecha"))
            {
                aux = aux.right;
            }
            else if(acciones.get(i_acciones).equals("adelante"))
            {
                aux = aux.next;
            }
            res.last.next = new NodeCircularLinkedList<String>();
            res.last.next.data = aux.coord;
            res.last = res.last.next;
            i_acciones++;
        }



        return res;
    }
}
