---
title: "Algoritmo de BinaryTree."
type: page
---

```cpp
#include <bits/stdc++.h>
using namespace std;

template <class T>
class bintree {
protected:
    /*
    Nodo que almacena internamente el elemento (de tipo T),
    y punteros al hijo izquierdo y derecho, que pueden ser
    nullptr si el hijo es vaco (no existe).
    */
    struct TreeNode;
    using Link = shared_ptr<TreeNode>;

    struct TreeNode {
        TreeNode(Link const& l, T const& e, Link const& r) : elem(e), left(l), right(r) {};
        T elem;
        Link left, right;
    };

    // constructora privada
    bintree(Link const& r) : raiz(r) {}

    // puntero a la raz del rbol
    Link raiz;

    private:
    void mostrar(Link const& raiz){
        if (raiz != this->raiz) cout << " ";
        if (raiz != nullptr){
            cout << raiz->elem;
            mostrar(raiz->left);
            mostrar(raiz->right);
        }
        else cout << -1;
    }


    void sumaleArbol(Link & raiz1, Link const & raiz2){
        if (raiz1 != nullptr && raiz2 != nullptr) {
            raiz1->elem += raiz2->elem;
            sumaleArbol(raiz1->left, raiz2->left);
            sumaleArbol(raiz1->right, raiz2->right);
        }
        else if (raiz1 == nullptr && raiz2 != nullptr) {
            raiz1 = raiz2;
        }

    }
    int height(Link const& node)
    {
       /* base case tree is empty */
       if(node == nullptr)
           return 0;

       /* If tree is not empty then height = 1 + max of left
          height and right heights */
       return 1 + max(height(node->left), height(node->right));
    }
    bool isBalanced(Link const& root)
    {
       int lh; /* for height of left subtree */
       int rh; /* for height of right subtree */

       /* If tree is empty then return true */
       if(root == nullptr) return 1;

       /* Get the height of left and right sub trees */
       lh = height(root->left);
       rh = height(root->right);
       if(root->left!=nullptr) { if(root->elem < root->left->elem) return 0; }
       if(root->right!=nullptr){ if(root->elem > root->right->elem) return 0; }
       if( abs(lh-rh) <= 1 &&isBalanced(root->left) && isBalanced(root->right)) return 1;

       /* If we reach here then tree is not height-balanced */
       return 0;
    }


public:
    int he()
    {
        return height(raiz);
    }
    void muestraArbol(){
        mostrar(raiz);
    }
    bool esAVL(){
        return isBalanced(raiz);
    }
    void sumaSobreArbol(bintree<T> const& arbol2){
        sumaleArbol(this->raiz, arbol2.raiz);
    }

    // rbol vaco
    bintree() : raiz(nullptr) {}

    // rbol hoja
    bintree(T const& e) :
        raiz(make_shared<TreeNode>(nullptr, e, nullptr)) {}

    // rbol con dos hijos
    bintree(bintree<T> const& l, T const& e, bintree<T> const& r) :
        raiz(make_shared<TreeNode>(l.raiz, e, r.raiz)) {}

    // consultar si el rbol est vaco
    bool empty() const {
        return raiz == nullptr;
    }

    // consultar la raz
    T const& root() const {
        if (empty()) throw domain_error("El arbol vacio no tiene raiz.");
        else return raiz->elem;
    }

    // consultar el hijo izquierdo
    bintree<T> left() const {
        if (empty()) throw domain_error("El arbol vacio no tiene hijo izquierdo.");
        else return bintree<T>(raiz->left);
    }

    // consultar el hijo derecho
    bintree<T> right() const {
        if (empty()) throw domain_error("El arbol vacio no tiene hijo derecho.");
        else return bintree(raiz->right);
    }


    // recorridos

    vector<T> preorder() const {
        vector<T> pre;
        preorder(raiz, pre);
        return pre;
    }

    vector<T> inorder() const {
        vector<T> in;
        inorder(raiz, in);
        return in;
    }

    vector<T> postorder() const {
        vector<T> post;
        postorder(raiz, post);
        return post;
    }

    vector<T> levelorder() const {
        vector<T> levels;
        if (!empty()) {
            queue<Link> pendientes;
            pendientes.push(raiz);
            while (!pendientes.empty()) {
                Link sig = pendientes.front();
                pendientes.pop();
                levels.push_back(sig->elem);
                if (sig->left != nullptr)
                    pendientes.push(sig->left);
                if (sig->right != nullptr)
                    pendientes.push(sig->right);
            }
        }
        return levels;
    }

protected:
    static void preorder(Link a, vector<T> & pre) {
        if (a != nullptr) {
            pre.push_back(a->elem);
            preorder(a->left, pre);
            preorder(a->right, pre);
        }
    }

    static void inorder(Link a, vector<T> & in) {
        if (a != nullptr) {
            inorder(a->left, in);
            in.push_back(a->elem);
            inorder(a->right, in);
        }
    }

    static void postorder(Link a, vector<T> & post) {
        if (a != nullptr) {
            postorder(a->left, post);
            postorder(a->right, post);
            post.push_back(a->elem);
        }
    }

public:
    // iterador que recorre el rbol en inorden
    class const_iterator {
    public:
        T const& operator*() const {
            if (ptr == nullptr) throw out_of_range("fuera del arbol");
            return ptr->elem;
        }

        T const* operator->() const {
            return &operator*();
        }

        bool operator==(const_iterator const& other) const {
            return ptr == other.ptr;
        }
        bool operator!=(const_iterator const& other) const {
            return !(*this == other);
        }

        const_iterator & operator++() {  // ++ prefijo
            next();
            return *this;
        }

    private:
        friend class bintree;
        Link ptr;
        stack<Link> ancestros;

        // constructores privados
        const_iterator() : ptr(nullptr) {}
        const_iterator(Link raiz) { ptr = first(raiz); }

        Link first(Link act) {
            if (act == nullptr) {
                return nullptr;
            }
            else {
                while (act->left != nullptr) {
                    ancestros.push(act);
                    act = act->left;
                }
                return act;
            }
        }

        void next() {
            if (ptr == nullptr) {
                throw range_error("El iterador no puede avanzar");
            }
            else if (ptr->right != nullptr) { // primero del hijo derecho
                ptr = first(ptr->right);
            }
            else if (ancestros.empty()) { // hemos llegado al final
                ptr = nullptr;
            }
            else { // podemos retroceder
                ptr = ancestros.top();
                ancestros.pop();
            }
        }

    };

    const_iterator begin() const {
        return const_iterator(raiz);
    }
    const_iterator end() const {
        return const_iterator();
    }

};

// lee un rbol binario de la entrada estndar
template <typename T>
inline bintree<T> leerArbol(T vacio) {
    T raiz;
    cin >> raiz;
    if (raiz == vacio) { // es un rbol vaco
        return{};
    }
    else { // leer recursivamente los hijos
        auto iz = leerArbol(vacio);
        auto dr = leerArbol(vacio);
        return{ iz, raiz, dr };
    }
}
bool resuelveCaso() {
    bintree <int> arbol1, arbol2;
    arbol1 = leerArbol(-1);
    arbol2 = leerArbol(-1);
    if (arbol1.empty() && arbol2.empty()) return false;
    arbol1.sumaSobreArbol(arbol2);
    arbol1.muestraArbol();
    cout << '\n';
    return true;
}
int main() {
    while (resuelveCaso());
    return 0;
}
```
