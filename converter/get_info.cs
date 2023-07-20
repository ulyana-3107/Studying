using System.Reflection;

class Program
{
    static void Main()
    {
        Assembly assembly = Assembly.LoadFrom("DLL_path");

        Console.WriteLine($"Assembly Name: {assembly.FullName}");
        Console.WriteLine($"Assembly Version: {assembly.GetName().Version}");

        Type[] types = assembly.GetTypes();

        foreach (Type type in types)
        {
            Console.WriteLine($"Type Name: {type.Name}");
            Console.WriteLine($"Type Namespace: {type.Namespace}");

            MemberInfo[] members = type.GetMembers();

            foreach (MemberInfo member in members)
            {
                Console.WriteLine($"Member Name: {member.Name}");
                Console.WriteLine($"Member Type: {member.MemberType}");
            }

            Console.WriteLine();
        }

        Console.ReadLine();
    }
}