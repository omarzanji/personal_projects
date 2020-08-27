package me.solofaze.LaunchCommand;


import org.bukkit.entity.Player;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import net.md_5.bungee.api.ChatColor;

public class Fly implements CommandExecutor {

	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		if (label.equalsIgnoreCase("launch") | label.equalsIgnoreCase("lch")) {
			if (!(sender instanceof Player)) {
				sender.sendMessage("*console goes flying*");
				return true;
			}
			Player player = (Player) sender;
			// /launch  / launch <number>
			if (args.length == 0) {
				// /launch
				player.sendMessage(ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + "Zooooom!");
				player.setVelocity(player.getLocation().getDirection().multiply(2).setY(2));
			}
			// /launch
			if (isNum(args[0])) { // checks that the player entered an "integer, not a string!
				player.sendMessage(ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + "Zooooom!");
				player.setVelocity(player.getLocation().getDirection().multiply(Integer.parseInt(args[0])).setY(2));
			} else {
				player.sendMessage(ChatColor.DARK_RED + "Usage: /launch <number-value>");
			}
			
			return true;
		}
		return false;
	}
	
	
	public boolean isNum(String num) {  // used for error catching player's command message
		try {
			Integer.parseInt(num);
		} catch (Exception e) {
			return false;
		}
		return true;
	}

}
