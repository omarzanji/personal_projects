package me.solofaze.FactionSelector;

import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.inventory.InventoryClickEvent;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;
import java.util.ArrayList;
import java.util.List;

import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import net.md_5.bungee.api.ChatColor;

public class Main extends JavaPlugin implements Listener {

	@Override
	public void onEnable() {
		this.getServer().getPluginManager().registerEvents(this, this); // allows us to listen to all events in Main class
	}

	
	@Override
	public void onDisable() {

	}

	
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		// command typed: "/faction_selector"
		if (label.equalsIgnoreCase("faction_selector")) {
			if (sender instanceof Player) {
				Player player = (Player) sender;
				player.getInventory().addItem(getItem("balance"));
				player.getInventory().addItem(getItem("turmoil"));
				player.sendMessage("Balance and Turmoil Item Selectors Generated");
				if (player.getInventory().firstEmpty() == -1) {
					//Inventory is full
					Location loc = player.getLocation();  // grab location!
					World world = player.getWorld();      // world drop!
					world.dropItemNaturally(loc, getItem("balance"));  // here's the drop! (location, and ItemStack param)
					world.dropItemNaturally(loc, getItem("turmoil"));  // "" above
					player.sendMessage("Inventory is full, check the ground!");   // amazing
					return true;
				}
				return true;
			} else {
				sender.sendMessage("Sorry console you're not allowed to BEPsI");
				return true;
			}
		}
		return false;
	}
	

	/**
	 * This function will create the ItemStack for the balance item.
	 * @param type - specify what item to generate.
	 */
	public ItemStack getItem (String type) {  // ItemStack is the Item Stack (the one that goes to 64)!
		
		if (type == null | type.length() == 0) {
			return null;
		}
		
		ItemStack balance = new ItemStack(Material.NETHER_STAR);  // Balance faction selector item
		ItemStack turmoil = new ItemStack(Material.ENDER_EYE);  // Turmoil faction selector item

		ItemMeta meta_balance = balance.getItemMeta(); // able to make custom metadata
		ItemMeta meta_turmoil = turmoil.getItemMeta();
		
		
		meta_balance.setDisplayName(ChatColor.GREEN + "" + ChatColor.BOLD + "Star of Balance");
		meta_turmoil.setDisplayName(ChatColor.RED + "" + ChatColor.BOLD + "Eye of Turmoil");

		List<String> lore_balance = new ArrayList<String>();
		List<String> lore_turmoil = new ArrayList<String>();
		
		lore_balance.add(""); // adds space under title !
		lore_balance.add(ChatColor.GREEN + "" + ChatColor.ITALIC + "select this item to join " + ChatColor.BOLD + "Balance");  // Balance
		meta_balance.setLore(lore_balance)
	//	meta_balance.;
		
		lore_turmoil.add(""); // adds space under title !
		lore_turmoil.add(ChatColor.RED + "" + ChatColor.ITALIC + "select this item to join " + ChatColor.BOLD + "Turmoil");  // Turmoil
		meta_turmoil.setLore(lore_turmoil);
		
		// meta.addEnchant and meta.addAttribute can be used
		balance.setItemMeta(meta_balance);
		turmoil.setItemMeta(meta_turmoil);
		
		if (type == "balance") return balance;
		else if (type == "turmoil") return turmoil;
		else return balance; 

	}
	
	
	/**
	 * Event handler to be called based on an event specified by the Listener.
	 * @param event - player event trigger data.
	 */
	@EventHandler
	public void onSelect(InventoryClickEvent event) {
		if (event.getWhoClicked() == null) {
			return;
		}
		//if (player.getInventory().contains(getItem("balance"))) {
		Player player = (Player) event.getWhoClicked();
		if (player.getItemOnCursor().getItemMeta().getDisplayName().contains("Star of Balance")) {
			//player.performCommand(""); // join dummy player's party "balance" located at Balance home teleport
			player.sendMessage("Welcome to Balance!");
		} else if (player.getItemOnCursor().getItemMeta().getDisplayName().contains("Eye of Turmoil")) {
			player.sendMessage("Welcome to Turmoil!");
		}
	}
	

}
