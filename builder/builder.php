<?php
class BuilderDesignPattern{
     public static void Main(string[] args)
        {
            Kid aKid = new Kid();
            aKid.Name = "Elizabeth";

            AnimalBuilder builderA = new MonkeyBuilder();
            aKid.MakeAnimal(builderA);
            builderA.aAnimal.ShowMe();

            AnimalBuilder builderB = new KittenBuilder();
            aKid.MakeAnimal(builderB);
            builderB.aAnimal.ShowMe();

        }
    }
    public abstract class AnimalBuilder
    {
        public Animal aAnimal;

        public abstract void BuildAnimalHeader();
        public abstract void BuildAnimalBody();
        public abstract void BuildAnimalLeg();
        public abstract void BuildAnimalArm();
        public abstract void BuildAnimalTail();
    }
    public class MonkeyBuilder : AnimalBuilder
    {

        public MonkeyBuilder()
        {
            aAnimal = new Monkey();
        }

        public override void BuildAnimalHeader()
        {
            aAnimal.Head = "Moneky's Head has been built";
        }

        public override void BuildAnimalBody()
        {
            aAnimal.Body = "Moneky's Body has been built";
        }

        public override void BuildAnimalLeg()
        {
            aAnimal.Leg = "Moneky's Leg has been built";
        }

        public override void BuildAnimalArm()
        {
            aAnimal.Arm = "Moneky's Arm has been built";
        }

        public override void BuildAnimalTail()
        {
            aAnimal.Tail = "Moneky's Tail has been built";
        }
    }
    public class KittenBuilder : AnimalBuilder
    {
        public KittenBuilder()
        {
            aAnimal = new Kitten();
        }

        public override void BuildAnimalHeader()
        {
            aAnimal.Head = "Kitten's Head has been built";
        }

        public override void BuildAnimalBody()
        {
            aAnimal.Body = "Kitten's Body has been built";
        }

        public override void BuildAnimalLeg()
        {
            aAnimal.Leg = "Kitten's Leg has been built";
        }

        public override void BuildAnimalArm()
        {
            aAnimal.Arm = "Kitten's Arm has been built";
        }

        public override void BuildAnimalTail()
        {
            aAnimal.Tail = "Kitten's Tail has been built";
        }
    }
    public abstract class Animal
    {
        public BodyPart Head { get; set; }
        public BodyPart Body { get; set; }
        public BodyPart Leg { get; set; }
        public BodyPart Arm { get; set; }
        public BodyPart Tail { get; set; }


        //helper method for demo the Polymorphism, so we can 
        //easily tell what type object it is from client.
        public abstract void Eat();

        //helper method for demo the result from client
        public void ShowMe()
        {
            Console.WriteLine(Head);
            Console.WriteLine(Body);
            Console.WriteLine(Leg);
            Console.WriteLine(Arm);
            Console.WriteLine(Tail);
            Eat();

        }
    }
    public class Monkey : Animal
    {
        //helper method to show monkey's property for demo purpose
        public override void Eat()
        {
            Console.WriteLine("Since I am Monkey, I like to eat banana");
        }
    }
    public class Kitten : Animal
    {
        public override void Eat()
        {
            Console.WriteLine("Since I am Kitten, I like to eat kitten food");
        }
    }
    public class Kid
    {
        public string Name { get; set; }

        //construct process to build an animal object, 
        //after this process completed, a object 
        //will be consider as a ready to use object.
        public void MakeAnimal(AnimalBuilder aAnimalBuilder)
        {
            aAnimalBuilder.BuildAnimalHeader();
            aAnimalBuilder.BuildAnimalBody();
            aAnimalBuilder.BuildAnimalLeg();
            aAnimalBuilder.BuildAnimalArm();
            aAnimalBuilder.BuildAnimalTail();
        }


    }
    public class BodyPart{
        String name= "";
        public BodyPart(String name){
            this.name=name;
        }
    }
}
?>