int main () {
    int a = 0;
    {
        a++;
        {
            a--;
        }
    }
    printf("%d", a);
}
