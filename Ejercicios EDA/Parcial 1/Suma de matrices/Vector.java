public class Vector {

    Node first;


    public Vector suma(Vector v1, Vector v2)
    {
        Vector vres = new Vector();
        vres.first = null;

        int pos = 0;
        Node act1 = v1.first;
        Node act2 = v2.first;
        Node act_vres = null;

        while(v1.first.next != null && v2.first.next != null)
        {
            if(act1.posicion == pos && act2.posicion == pos)
            {
                if(act_vres == null)
                {
                    act_vres = new Node(pos, act1.dato + act2.dato);
                    vres.first = act_vres;
                }
                else
                {
                    act_vres.next = new Node(pos, act1.dato + act2.dato);
                    act_vres = act_vres.next;
                }
            }
            else
            {
                if(act1.posicion == pos)
                {
                    if(act_vres == null)
                    {
                        act_vres = new Node(pos, act1.dato + act2.dato);
                        vres.first = act_vres;
                    }
                    else
                    {
                        act_vres.next = new Node(pos,act1.dato + act2.dato);
                        act_vres = act_vres.next;
                    }
                }
                else if(act2.posicion == pos)
                {
                    if(act_vres == null)
                    {
                        act_vres = new Node(pos, act1.dato + act2.dato);
                        vres.first = act_vres;
                    }
                    else
                    {
                        act_vres.next = new Node(pos,act1.dato + act2.dato);
                        act_vres = act_vres.next;
                    }

                }
                act1 = act1.next;
                act2 = act2.next;
            }
        }

        return vres;
    }
}
