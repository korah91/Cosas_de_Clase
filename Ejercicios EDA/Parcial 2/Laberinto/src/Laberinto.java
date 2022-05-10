import java.util.*;

public class Laberinto{
    public int[][] laberinto={{1.1...},...};
    public boolean traverse(){
        //entrada extremos superior izquierdo salida extremo inferior derecho
        Stack<Casilla> porExaminar = new Stack<Casilla>();
        Casilla inicio = new Casilla(0,0);
        posExaminar.push(inicio);
        Casilla fin = new Casilla(this.laberinto.length()-1,this.laberinto[0].length()-1);
        boolean[][] examinados = new [this.laberinto.length()][this.laberinto[0].length()];
        examinados[0][0]=true;
        boolean enc=false;
        while(!porExaminar.isEmpty()&&!enc){
        Casilla act=porExaminar.pop();
        if(act.compareTo(fin)==0){
        enc=true;
        }
        else{
        if(dentro(act.x-1,act.y)&& laberinto[act.x-1][act.y] && !examinados[act.x-1][act.y]){
        Casilla nuevo = new Casilla(act.x-1,act.y);
        porExaminar.push(nuevo);
        examinados[act.x-1,act.y]=True;
        }
        if(dentro(act.x-1,act.y)&& laberinto[act.x-1][act.y] && !examinados[act.x-1][act.y]){
        Casilla nuevo = new Casilla(act.x-1,act.y);
        porExaminar.push(nuevo);
        examinados[act.x-1,act.y]=True;
        }
        if(dentro(act.x,act.y-1)&& laberinto[act.x][act.y-1] && !examinados[act.x][act.y-1]){
        Casilla nuevo = new Casilla(act.x,act.y-1);
        porExaminar.push(nuevo);
        examinados[act.x,act.y-1]=True;
        }
        if(dentro(act.x-1,act.y-1)&& laberinto[act.x-1][act.y-1] && !examinados[act.x-1][act.y-1]){
        Casilla nuevo = new Casilla(act.x-1,act.y-1);
        porExaminar.push(nuevo);
        examinados[act.x,act.y-1]=True;
        }
        }
        }
        return enc;
        }
        }
public class Casilla{
    int x;
    int y;
    public Casilla(int pX, int pY){
        this.x=pX;
        this.y=pY;
    }
    public int compareTo(Casilla pCas){
        if(this.x>pCas.x){
            return 1;
        }
        else if(pCas.x>this.x){
            return -1;
        }
        else{
            if(pCas.y==this.y){
                return 0
            }
            else if(pCas.y>this.y){
                return -1
            }
            else{return 1}
        }
    }
}
//Codigo sin java
/*
porExaminar=()
examinadas=()
com=(0,0)
fin=(n,m)
porExaminar.anadir(com);
examinados.anadir(com);
enc=false
while porExaminar!=()&& enc=false{
	actual=porExaminar.borrar()
	if(actual==fin){
		enc=true;
	}
	else{
		para cada x pertencientes a sucesores(act);
		if(x no examinado){
			porExaminar.anadir(x)
			examinados.anadir(x)
		}
	}
}
return enc
*/