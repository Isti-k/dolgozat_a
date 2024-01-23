def eldont():
    elsoSzo=input("Kérek egy szót:")
    masodikSzo=input("Kérek egy második szót:")
    print()
    if len(elsoSzo)> len(masodikSzo):
        print(f"\t A hosszabb szó:{elsoSzo}")
    elif len(elsoSzo) < len(masodikSzo):
         print(f"\t A hosszabb szó:{masodikSzo}")
    else:
        print(f"\t Egyforma hosszúak.")
    print("I/d.")
    print(f"\t A szavak hosszának külömbsége: {abs(len(elsoSzo)-len(masodikSzo))}")

def egy():
    eldont()

