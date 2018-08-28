@AoA = (
    [1,2,3],
    [4,5,6],
    [7,8,9],
);
print "AoA:\n";
print "@{$_}\n" for @AoA;
print "\n\n";

@AoH = (
    {
        one => "11",
        two => "22",
        three => "33",
    },
    {
        one => "111",
        two => "222",
        three => "333",
    },
    {
        one => "1111",
        two => "2222",
        three => "3333",
    },
);
print "AoH:\n";
for my $h (@AoH) {
    print "$_: $$h{$_}\n" for keys %{$h};
    print "====\n";
}
print "\n\n";

%HoA = (
    one => [1,2,3],
    two => [4,5,6],
    three => [7,8,9],
);
print "HoA:\n";
print "$_: @{$HoA{$_}}\n" for keys %HoA;
print "\n\n";

%HoH = (
    "true" => {
        one => "11",
        two => "22",
        three => "33",
    },
    "false" => {
        one => "111",
        two => "222",
        three => "333",
    },
    "maybe" => {
        one => "1111",
        two => "2222",
        three => "3333",
    },
);

print "HoH:\n";
for my $h (keys %HoH) {
    print "$h: $_: ${$HoH{$h}}{$_}\n" for keys %{$HoH{$h}};
    print "====\n";
}
